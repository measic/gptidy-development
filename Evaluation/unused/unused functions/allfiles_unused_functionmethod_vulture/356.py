class GenerativeNetwork:

    def __init__(self, img_width=96, img_height=96, batch_size=16, num_upscales=2, small_model=False,
                 content_weight=1, tv_weight=2e5, gen_channels=64):
        self.img_width = img_width
        self.img_height = img_height
        self.batch_size = batch_size
        self.small_model = small_model
        self.num_scales = num_upscales

        self.content_weight = content_weight
        self.tv_weight = tv_weight

        self.filters = gen_channels
        self.mode = 2
        self.init = 'glorot_uniform'

        self.sr_res_layers = None
        self.sr_weights_path = "weights/SRGAN.h5"

        self.output_func = None

    def create_sr_model(self, ip):

        x = Conv2D(self.filters, (5, 5), activation='linear', padding='same', name='sr_res_conv1',
                          kernel_initializer=self.init)(ip)
        x = BatchNormalization(axis=channel_axis, name='sr_res_bn_1')(x)
        x = LeakyReLU(alpha=0.25, name='sr_res_lr1')(x)

        x = Conv2D(self.filters, (5, 5), activation='linear', padding='same', name='sr_res_conv2', kernel_initializer="glorot_uniform")(x)
        x = BatchNormalization(axis=channel_axis, name='sr_res_bn_2')(x)
        x = LeakyReLU(alpha=0.25, name='sr_res_lr2')(x)

        num_residual = 5 if self.small_model else 15

        for i in range(num_residual):
            x = self._residual_block(x, i + 1)

        for scale in range(self.num_scales):
            x = self._upscale_block(x, scale + 1)
    
        scale = 2 ** self.num_scales
        tv_regularizer = TVRegularizer(img_width=self.img_width * scale, img_height=self.img_height * scale,
                                       weight=self.tv_weight) #self.tv_weight)
        
        x = Conv2D(3, (5, 5), activation='tanh', padding='same', activity_regularizer=tv_regularizer, 
                   name='sr_res_conv_final', kernel_initializer=self.init)(x)
        
        x = Denormalize(name='sr_res_conv_denorm')(x)
        return x

    def _residual_block(self, ip, id):
        init = ip

        x = Conv2D(self.filters, (3, 3), activation='linear', padding='same', name='sr_res_conv_' + str(id) + '_1',
                          kernel_initializer=self.init)(ip)
        x = BatchNormalization(axis=channel_axis, name='sr_res_bn_' + str(id) + '_1')(x)
        x = LeakyReLU(alpha=0.25, name="sr_res_activation_" + str(id) + "_1")(x)

        x = Conv2D(self.filters, (3, 3), activation='linear', padding='same', name='sr_res_conv_' + str(id) + '_2',
                          kernel_initializer=self.init)(x)
        x = BatchNormalization(axis=channel_axis, name='sr_res_bn_' + str(id) + '_2')(x)

        m = add([x, init],name="sr_res_merge_" + str(id))

        return m

    def _upscale_block(self, ip, id):
        '''
        As per suggestion from http://distill.pub/2016/deconv-checkerboard/, I am swapping out
        SubPixelConvolution to simple Nearest Neighbour Upsampling
        '''
        init = ip
        
        x = Conv2D(128, (3, 3), activation="linear", padding='same', name='sr_res_upconv1_%d' % id,
                          kernel_initializer=self.init)(init)
        x = LeakyReLU(alpha=0.25, name='sr_res_up_lr_%d_1_1' % id)(x)
        x = UpSampling2D(name='sr_res_upscale_%d' % id)(x)
        #x = SubPixelUpscaling(r=2, channels=32)(x)
        x = Conv2D(128, (3, 3), activation="linear", padding='same', name='sr_res_filter1_%d' % id,
                          kernel_initializer=self.init)(x)
        x = LeakyReLU(alpha=0.3, name='sr_res_up_lr_%d_1_2' % id)(x)

        return x

    def set_trainable(self, model, value=True):
        if self.sr_res_layers is None:
            self.sr_res_layers = [layer for layer in model.layers
                                    if 'sr_res_' in layer.name]

        for layer in self.sr_res_layers:
            layer.trainable = value

    def get_generator_output(self, input_img, srgan_model):
        if self.output_func is None:
            gen_output_layer = [layer for layer in srgan_model.layers
                                if layer.name == "sr_res_conv_denorm"][0]
            self.output_func = K.function([srgan_model.layers[0].input],
                                          [gen_output_layer.output])

        return self.output_func([input_img])