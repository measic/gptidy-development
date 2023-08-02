class SRGANNetwork:

    def __init__(self, img_width=96, img_height=96, batch_size=16, num_scales=2):
        self.img_width = img_width
        self.img_height = img_height
        self.batch_size = batch_size
        self.num_scales = num_scales

        self.discriminative_network = None # type: DiscriminatorNetwork
        self.generative_network = None # type: GenerativeNetwork
        self.vgg_network = None # type: VGGNetwork

        self.srgan_model_ = None # type: Model
        self.generative_model_ = None # type: Model
        self.discriminative_model_ = None #type: Model

    def build_srgan_pretrain_model(self, use_small_srgan=False):
        large_width = self.img_width * 4
        large_height = self.img_height * 4

        self.generative_network = GenerativeNetwork(self.img_width, self.img_height, self.batch_size, self.num_scales,
                                                    use_small_srgan)
        self.vgg_network = VGGNetwork(large_width, large_height)

        ip = Input(shape=(self.img_width, self.img_height, 3), name='x_generator')
        ip_vgg = Input(shape=(large_width, large_height, 3), name='x_vgg')  # Actual X images

        sr_output = self.generative_network.create_sr_model(ip)
        self.generative_model_ = Model(ip, sr_output)

        vgg_output = self.vgg_network.append_vgg_network(sr_output, ip_vgg, pre_train=True)

        self.srgan_model_ = Model(inputs=[ip, ip_vgg],
                                  outputs=vgg_output)

        self.vgg_network.load_vgg_weight(self.srgan_model_)

        srgan_optimizer = Adam(lr=1e-4)
        generator_optimizer = Adam(lr=1e-4)

        self.generative_model_.compile(generator_optimizer, dummy_loss)
        self.srgan_model_.compile(srgan_optimizer, dummy_loss)

        return self.srgan_model_


    def build_discriminator_pretrain_model(self, use_small_srgan=False, use_small_discriminator=False):
        large_width = self.img_width * 4
        large_height = self.img_height * 4

        self.generative_network = GenerativeNetwork(self.img_width, self.img_height, self.batch_size, self.num_scales,
                                                    use_small_srgan)
        self.discriminative_network = DiscriminatorNetwork(large_width, large_height,
                                                           small_model=use_small_discriminator)

        ip = Input(shape=(self.img_width, self.img_height, 3), name='x_generator')
        ip_gan = Input(shape=(large_width, large_height, 3), name='x_discriminator')  # Actual X images

        sr_output = self.generative_network.create_sr_model(ip)
        self.generative_model_ = Model(ip, sr_output)
        #self.generative_network.set_trainable(self.generative_model_, value=False)

        gan_output = self.discriminative_network.append_gan_network(ip_gan)
        self.discriminative_model_ = Model(ip_gan, gan_output)

        generator_out = self.generative_model_(ip)
        gan_output = self.discriminative_model_(generator_out)

        self.srgan_model_ = Model(inputs=ip, outputs=gan_output)

        srgan_optimizer = Adam(lr=1e-4)
        generator_optimizer = Adam(lr=1e-4)
        discriminator_optimizer = Adam(lr=1e-4)

        self.generative_model_.compile(generator_optimizer, loss='mse')
        self.discriminative_model_.compile(discriminator_optimizer, loss='categorical_crossentropy', metrics=['acc'])
        self.srgan_model_.compile(srgan_optimizer, loss='categorical_crossentropy', metrics=['acc'])



        return self.discriminative_model_


    def build_srgan_model(self, use_small_srgan=False, use_small_discriminator=False):
        large_width = self.img_width * 4
        large_height = self.img_height * 4

        self.generative_network = GenerativeNetwork(self.img_width, self.img_height, self.batch_size, num_upscales=self.num_scales,
                                                    small_model=use_small_srgan)
        self.discriminative_network = DiscriminatorNetwork(large_width, large_height,
                                                           small_model=use_small_discriminator)
        self.vgg_network = VGGNetwork(large_width, large_height)

        ip = Input(shape=(self.img_width, self.img_height, 3), name='x_generator')
        ip_gan = Input(shape=(large_width, large_height, 3), name='x_discriminator') # Actual X images
        ip_vgg = Input(shape=(large_width, large_height, 3), name='x_vgg') # Actual X images
        sr_output = self.generative_network.create_sr_model(ip)
        self.generative_model_ = Model(ip, sr_output)

        gan_output = self.discriminative_network.append_gan_network(ip_gan)
        self.discriminative_model_ = Model(ip_gan, gan_output)        
        gan_output = self.discriminative_model_(self.generative_model_.output)
        vgg_output = self.vgg_network.append_vgg_network(self.generative_model_.output, ip_vgg)

        self.srgan_model_ = Model(inputs=[ip, ip_gan, ip_vgg], outputs=[gan_output, vgg_output])

        self.vgg_network.load_vgg_weight(self.srgan_model_)

        srgan_optimizer = Adam(lr=1e-4)
        generator_optimizer = Adam(lr=1e-4)
        discriminator_optimizer = Adam(lr=1e-4)

        self.generative_model_.compile(generator_optimizer, dummy_loss)
        self.discriminative_model_.compile(discriminator_optimizer, loss='categorical_crossentropy', metrics=['acc'])
        self.srgan_model_.compile(srgan_optimizer, dummy_loss)

        return self.srgan_model_


    def pre_train_srgan(self, image_dir, num_images=50000, epochs=1, use_small_srgan=False):
        self.build_srgan_pretrain_model(use_small_srgan=use_small_srgan)

        self._train_model(image_dir, num_images=num_images, epochs=epochs, pre_train_srgan=True,
                          load_generative_weights=True)

    def pre_train_discriminator(self, image_dir, num_images=50000, epochs=1, batch_size=128,
                                use_small_discriminator=False):

        self.batch_size = batch_size
        self.build_discriminator_pretrain_model(use_small_discriminator)

        self._train_model(image_dir, num_images, epochs, pre_train_discriminator=True,
                          load_generative_weights=True)

    def train_full_model(self, image_dir, num_images=50000, epochs=10, batch_size=128, use_small_srgan=False,
                         use_small_discriminator=False):
        self.batch_size = batch_size
        self.build_srgan_model(use_small_srgan, use_small_discriminator)

        self._train_model(image_dir, num_images, epochs, load_generative_weights=True, load_discriminator_weights=True)

    def _train_model(self, image_dir, num_images=80000, epochs=10, pre_train_srgan=False,
                     pre_train_discriminator=False, load_generative_weights=False, load_discriminator_weights=False,
                     save_loss=True, disc_train_flip=0.1):

        assert self.img_width >= 16, "Minimum image width must be at least 16"
        assert self.img_height >= 16, "Minimum image height must be at least 16"

        if load_generative_weights:
            try:
                self.generative_model_.load_weights(self.generative_network.sr_weights_path)
                print("Generator weights loaded.")
            except:
                print("Could not load generator weights.")

        if load_discriminator_weights:
            try:
                self.discriminative_network.load_gan_weights(self.srgan_model_)
                print("Discriminator weights loaded.")
            except:
                print("Could not load discriminator weights.")

        datagen = ImageDataGenerator(rescale=1. / 255)
        img_width = self.img_width * 4
        img_height = self.img_height * 4

        early_stop = False
        iteration = 0
        prev_improvement = -1

        if save_loss:
            if pre_train_srgan:
                loss_history = {'generator_loss' : [],
                                'val_psnr' : [], }
            elif pre_train_discriminator:
                loss_history = {'discriminator_loss' : [],
                                'discriminator_acc' : [], }
            else:
                loss_history = {'discriminator_loss' : [],
                                'discriminator_acc' : [],
                                'generator_loss' : [],
                                'val_psnr': [], }

        y_vgg_dummy = np.zeros((self.batch_size * 2, 3, img_width // 32, img_height // 32)) # 5 Max Pools = 2 ** 5 = 32

        print("Training SRGAN network")
        for i in range(epochs):
            print()
            print("Epoch : %d" % (i + 1))
            for x in datagen.flow_from_directory(image_dir, class_mode=None, batch_size=self.batch_size,
                                                 target_size=(img_width, img_height)):
                try:
                    t1 = time.time()

                    if not pre_train_srgan and not pre_train_discriminator:
                        x_vgg = x.copy() * 255 # VGG input [0 - 255 scale]

                    # resize images
                    x_temp = x.copy()
                    x_temp = x_temp.transpose((0, 2, 3, 1))

                    x_generator = np.empty((self.batch_size, self.img_width, self.img_height, 3))
                    def shift_down(xy):                        
                        return xy
                    
                    for j in range(self.batch_size):
                        img = gaussian_filter(x_temp[j], sigma=0.1)
                        img = imresize(img, (self.img_width, self.img_height), interp='bicubic')
                        #img = resize(img, (self.img_width, self.img_height))
                        x_generator[j, :, :, :] = img

                    #x_generator = x_generator.transpose((0, 3, 1, 2))

                    if iteration % 50 == 0 and iteration != 0 and not pre_train_discriminator:
                        print("Validation image..")
                        output_image_batch = self.generative_network.get_generator_output(x_generator,
                                                                                          self.srgan_model_)
                        if type(output_image_batch) == list:
                            output_image_batch = output_image_batch[0]

                        mean_axis = (0, 2, 3) if K.image_dim_ordering() == 'th' else (0, 1, 2)

                        average_psnr = 0.0

                        print('gen img mean :', np.mean(output_image_batch / 255., axis=mean_axis))
                        print('val img mean :', np.mean(x, axis=mean_axis))

                        for x_i in range(self.batch_size):
                            average_psnr += psnr(x[x_i], np.clip(output_image_batch[x_i], 0, 255) / 255.)

                        average_psnr /= self.batch_size

                        if save_loss:
                            loss_history['val_psnr'].append(average_psnr)

                        iteration += self.batch_size
                        t2 = time.time()

                        print("Time required : %0.2f. Average validation PSNR over %d samples = %0.2f" %
                              (t2 - t1, self.batch_size, average_psnr))

                        for x_i in range(self.batch_size):
                            real_path = "val_images/epoch_%d_iteration_%d_num_%d_real_.png" % (i + 1, iteration, x_i + 1)
                            generated_path = "val_images/epoch_%d_iteration_%d_num_%d_generated.png" % (i + 1,
                                                                                                        iteration,
                                                                                                        x_i + 1)

                            val_x = x[x_i].copy() * 255.
                            #val_x = val_x.transpose((1, 2, 0))
                            val_x = np.clip(val_x, 0, 255).astype('uint8')

                            output_image = output_image_batch[x_i]
                            #output_image = output_image.transpose((1, 2, 0))
                            output_image = np.clip(output_image, 0, 255).astype('uint8')

                            imsave(real_path, val_x[:,:,0])
                            imsave(generated_path, output_image[:,:,0])

                        '''
                        Don't train of validation images for now.

                        Note that if epochs > 1, there is a chance that
                        validation images may be used for training purposes as well.

                        In that case, this isn't strictly a validation measure, instead of
                        just a check to see what the network has learned.
                        '''
                        continue

                    if pre_train_srgan:
                        # Train only generator + vgg network

                        # Use custom bypass_fit to bypass the check for same input and output batch size
                        hist = bypass_fit(self.srgan_model_, [x_generator, x * 255], y_vgg_dummy,
                                                     batch_size=self.batch_size, epochs=1, verbose=0)
                        sr_loss = hist.history['loss'][0]

                        if save_loss:
                            loss_history['generator_loss'].extend(hist.history['loss'])

                        if prev_improvement == -1:
                            prev_improvement = sr_loss

                        improvement = (prev_improvement - sr_loss) / prev_improvement * 100
                        prev_improvement = sr_loss

                        iteration += self.batch_size
                        t2 = time.time()

                        print("%d / %d | Improvement : %0.2f %% | %0.2f s/steps | "
                              "GLoss: %0.2f" % (iteration, num_images, improvement, t2 - t1, sr_loss))
                    elif pre_train_discriminator:
                        # Train only discriminator
                        X_pred = self.generative_model_.predict(x_generator, self.batch_size)

                        X = np.concatenate((X_pred, x * 255))

                        # Using soft and noisy labels
                        if np.random.uniform() > disc_train_flip:
                            # give correct classifications
                            y_gan = [0] * self.batch_size + [1] * self.batch_size
                        else:
                            # give wrong classifications (noisy labels)
                            y_gan = [1] * self.batch_size + [0] * self.batch_size

                        y_gan = np.asarray(y_gan, dtype=np.int).reshape(-1, 1)
                        y_gan = to_categorical(y_gan, num_classes=2)
                        y_gan = smooth_gan_labels(y_gan)

                        hist = self.discriminative_model_.fit(X, y_gan, batch_size=self.batch_size,
                                                              epochs=1, verbose=0)

                        discriminator_loss = hist.history['loss'][-1]
                        discriminator_acc = hist.history['acc'][-1]

                        if save_loss:
                            loss_history['discriminator_loss'].extend(hist.history['loss'])
                            loss_history['discriminator_acc'].extend(hist.history['acc'])

                        if prev_improvement == -1:
                            prev_improvement = discriminator_loss

                        improvement = (prev_improvement - discriminator_loss) / prev_improvement * 100
                        prev_improvement = discriminator_loss

                        iteration += self.batch_size
                        t2 = time.time()

                        print("%d / %d | Improvement : %0.2f %% | %0.2f s/step | "
                            "DLoss/Acc : %0.4f / %0.2f" % (iteration, num_images,
                                                            improvement, t2 - t1,
                                                            discriminator_loss, discriminator_acc))

                    else:
                        # Train only discriminator, disable training of srgan
                        self.discriminative_network.set_trainable(self.srgan_model_, value=True)
                        self.generative_network.set_trainable(self.srgan_model_, value=False)

                        # Use custom bypass_fit to bypass the check for same input and output batch size
                        # hist = bypass_fit(self.srgan_model_, [x_generator, x * 255, x_vgg],
                        #                          [y_gan, y_vgg_dummy],
                        #                          batch_size=self.batch_size, epochs=1, verbose=0)

                        X_pred = self.generative_model_.predict(x_generator, self.batch_size)

                        X = np.concatenate((X_pred, x * 255))

                        # Using soft and noisy labels
                        if np.random.uniform() > disc_train_flip:
                            # give correct classifications
                            y_gan = [0] * self.batch_size + [1] * self.batch_size
                        else:
                            # give wrong classifications (noisy labels)
                            y_gan = [1] * self.batch_size + [0] * self.batch_size

                        y_gan = np.asarray(y_gan, dtype=np.int).reshape(-1, 1)
                        y_gan = to_categorical(y_gan, num_classes=2)
                        y_gan = smooth_gan_labels(y_gan)

                        hist1 = self.discriminative_model_.fit(X, y_gan, verbose=0, batch_size=self.batch_size,
                                                              epochs=1)

                        discriminator_loss = hist1.history['loss'][-1]

                        # Train only generator, disable training of discriminator
                        self.discriminative_network.set_trainable(self.srgan_model_, value=False)
                        self.generative_network.set_trainable(self.srgan_model_, value=True)

                        # Using soft labels
                        y_model = [1] * self.batch_size
                        y_model = np.asarray(y_model, dtype=np.int).reshape(-1, 1)
                        y_model = to_categorical(y_model, num_classes=2)
                        y_model = smooth_gan_labels(y_model)

                        # Use custom bypass_fit to bypass the check for same input and output batch size
                        hist2 = bypass_fit(self.srgan_model_, [x_generator, x, x_vgg], [y_model, y_vgg_dummy],
                                           batch_size=self.batch_size, epochs=1, verbose=0)

                        generative_loss = hist2.history['loss'][0]

                        if save_loss:
                            loss_history['discriminator_loss'].extend(hist1.history['loss'])
                            loss_history['discriminator_acc'].extend(hist1.history['acc'])
                            loss_history['generator_loss'].extend(hist2.history['loss'])

                        if prev_improvement == -1:
                            prev_improvement = discriminator_loss

                        improvement = (prev_improvement - discriminator_loss) / prev_improvement * 100
                        prev_improvement = discriminator_loss

                        iteration += self.batch_size
                        t2 = time.time()
                        print("%d / %d | Improvement : %0.2f %% | %0.2f s/step | DLoss : %0.3f | GLoss : %0.3f" %
                              (iteration, num_images, improvement, t2 - t1, discriminator_loss, generative_loss))

                    if iteration % 1000 == 0 and iteration != 0:
                        print("Saving model weights.")
                        # Save predictive (SR network) weights
                        self._save_model_weights(pre_train_srgan, pre_train_discriminator)
                        self._save_loss_history(loss_history, pre_train_srgan, pre_train_discriminator, save_loss)

                    if iteration >= num_images:
                        break

                except KeyboardInterrupt:
                    print("Keyboard interrupt detected. Stopping early.")
                    early_stop = True
                    break

            iteration = 0

            if early_stop:
                break

        print("Finished training SRGAN network. Saving model weights.")
        # Save predictive (SR network) weights
        self._save_model_weights(pre_train_srgan, pre_train_discriminator)
        self._save_loss_history(loss_history, pre_train_srgan, pre_train_discriminator, save_loss)

    def _save_model_weights(self, pre_train_srgan, pre_train_discriminator):
        if not pre_train_discriminator:
            self.generative_model_.save_weights(self.generative_network.sr_weights_path, overwrite=True)

        if not pre_train_srgan:
            # Save GAN (discriminative network) weights
            self.discriminative_network.save_gan_weights(self.discriminative_model_)

    def _save_loss_history(self, loss_history, pre_train_srgan, pre_train_discriminator, save_loss):
        if save_loss:
            print("Saving loss history")

            if pre_train_srgan:
                with open('pretrain losses - srgan.json', 'w') as f:
                    json.dump(loss_history, f)
            elif pre_train_discriminator:
                with open('pretrain losses - discriminator.json', 'w') as f:
                    json.dump(loss_history, f)
            else:
                with open('fulltrain losses.json', 'w') as f:
                    json.dump(loss_history, f)

            print("Saved loss history")