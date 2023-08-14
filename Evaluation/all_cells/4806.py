class SRResNetTest:

    def __init__(self, img_width=96, img_height=96, batch_size=16):
        assert img_width >= 16, "Minimum image width must be at least 16"
        assert img_height >= 16, "Minimum image height must be at least 16"

        self.img_width = img_width
        self.img_height = img_height
        self.batch_size = batch_size

        self.model = None # type: Model
        self.weights_path = base_weights_path + "sr_resnet_weights.h5"

    def build_model(self, load_weights=False) -> Model:
        sr_resnet = GenerativeNetwork(self.img_width, self.img_height, self.batch_size)

        ip = Input(shape=(self.img_width, self.img_height, 3), name='x_generator')
        output = sr_resnet.create_sr_model(ip)

        self.model = Model(ip, output)

        optimizer = Adam(lr=1e-4)
        self.model.compile(optimizer, loss='mse', metrics=[PSNRLoss])

        if load_weights:
            try:
                self.model.load_weights(self.weights_path)
                print("SR ResNet model weights loaded.")
            except Exception:
                print("Weight for SR ResNet model not found or are incorrect size. Cannot load weights.")

                response = input("Continue without loading weights? 'y' or 'n' ")
                if response == 'n':
                    exit()

        return self.model

    def train_model(self, image_dir, num_images=50000, epochs=1):
        datagen = ImageDataGenerator(rescale=1. / 255)
        img_width = self.img_width * 4
        img_height = self.img_height * 4

        early_stop = False
        iteration = 0
        prev_improvement = -1

        print("Training SR ResNet network")
        for i in range(epochs):
            print()
            print("Epoch : %d" % (i + 1))

            for x in datagen.flow_from_directory(image_dir, class_mode=None, batch_size=self.batch_size,
                                                 target_size=(img_width, img_height)):

                try:
                    t1 = time.time()

                    # resize images
                    x_temp = x.copy()
                    x_temp = x_temp.transpose((0, 2, 3, 1))

                    x_generator = np.empty((self.batch_size, self.img_width, self.img_height, 3))

                    for j in range(self.batch_size):
                        img = gaussian_filter(x_temp[j], sigma=0.5)
                        img = imresize(img, (self.img_width, self.img_height))
                        x_generator[j, :, :, :] = img

                    #x_generator = x_generator.transpose((0, 3, 1, 2))

                    if iteration % 50 == 0 and iteration != 0 :
                        print("Random Validation image..")
                        output_image_batch = self.model.predict_on_batch(x_generator)

                        print("Pred Max / Min: %0.2f / %0.2f" % (output_image_batch.max(),
                                                                 output_image_batch.min()))

                        average_psnr = 0.0
                        for x_i in range(self.batch_size):
                            average_psnr += psnr(x[x_i], output_image_batch[x_i] / 255.)

                        average_psnr /= self.batch_size

                        iteration += self.batch_size
                        t2 = time.time()

                        print("Time required : %0.2f. Average validation PSNR over %d samples = %0.2f" %
                              (t2 - t1, self.batch_size, average_psnr))

                        for x_i in range(self.batch_size):
                            real_path = base_val_images_path + "epoch_%d_iteration_%d_num_%d_real_.png" % \
                                                               (i + 1, iteration, x_i + 1)

                            generated_path = base_val_images_path + \
                                             "epoch_%d_iteration_%d_num_%d_generated.png" % (i + 1,
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

                    hist = self.model.fit(x_generator, x * 255, batch_size=self.batch_size, epochs=1, verbose=0)
                    psnr_loss_val = hist.history['PSNRLoss'][0]

                    if prev_improvement == -1:
                        prev_improvement = psnr_loss_val

                    improvement = (prev_improvement - psnr_loss_val) / prev_improvement * 100
                    prev_improvement = psnr_loss_val

                    iteration += self.batch_size
                    t2 = time.time()

                    print("%d / %d | Improvement : %0.2f %% | Time required : %0.2f s/step | "
                          "PSNR : %0.3f" % (iteration, num_images, improvement, t2 - t1, psnr_loss_val))

                    if iteration % 1000 == 0 and iteration != 0:
                        print("Saving weights")
                        self.model.save_weights(self.weights_path, overwrite=True)

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