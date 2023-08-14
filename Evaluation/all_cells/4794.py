class VGGNetwork:
    '''
    Helper class to load VGG and its weights to the FastNet model
    '''

    def __init__(self, img_width=384, img_height=384, vgg_weight=1.0):
        self.img_height = img_height
        self.img_width = img_width
        self.vgg_weight = vgg_weight

        self.vgg_layers = None

    def append_vgg_network(self, x_in, true_X_input, pre_train=False):

        # Append the initial inputs to the outputs of the SRResNet
        x = concatenate([x_in, true_X_input], axis=0)

        # Normalize the inputs via custom VGG Normalization layer
        x = Normalize(name="normalize_vgg")(x)

        # Begin adding the VGG layers
        x = Conv2D(64, (3, 3), activation='relu', padding='same', name='vgg_conv1_1')(x)

        x = Conv2D(64, (3, 3), activation='relu', padding='same', name='vgg_conv1_2')(x)
        x = MaxPooling2D((2, 2), strides=(2, 2), name='vgg_maxpool1')(x)

        x = Conv2D(128, (3, 3), activation='relu', padding='same', name='vgg_conv2_1')(x)

        vgg_regularizer2 = ContentVGGRegularizer(weight=self.vgg_weight)
        x = Conv2D(128, (3, 3), activation='relu', padding='same',
                              activity_regularizer=vgg_regularizer2, name='vgg_conv2_2')(x)
        
        x = MaxPooling2D((2, 2), strides=(2, 2), name='vgg_maxpool2')(x)

        x = Conv2D(256, (3, 3), activation='relu', padding='same', name='vgg_conv3_1')(x)
        x = Conv2D(256, (3, 3), activation='relu', padding='same', name='vgg_conv3_2')(x)

        x = Conv2D(256, (3, 3), activation='relu', padding='same', name='vgg_conv3_3')(x)
        x = MaxPooling2D((2, 2), strides=(2, 2), name='vgg_maxpool3')(x)

        x = Conv2D(512, (3, 3), activation='relu', padding='same', name='vgg_conv4_1')(x)
        x = Conv2D(512, (3, 3), activation='relu', padding='same', name='vgg_conv4_2')(x)

        x = Conv2D(512, (3, 3), activation='relu', padding='same', name='vgg_conv4_3')(x)
        x = MaxPooling2D((2, 2), strides=(2, 2), name='vgg_maxpool4')(x)

        x = Conv2D(512, (3, 3), activation='relu', padding='same', name='vgg_conv5_1')(x)
        x = Conv2D(512, (3, 3), activation='relu', padding='same', name='vgg_conv5_2')(x)

        x = Conv2D(512, (3, 3), activation='relu', padding='same', name='vgg_conv5_3')(x)
        x = MaxPooling2D((2, 2), strides=(2, 2), name='vgg_maxpool5')(x)

        return x

    def load_vgg_weight(self, model):
        # Loading VGG 16 weights
        if K.image_dim_ordering() == "th":
            weights = get_file('vgg16_weights_th_dim_ordering_th_kernels_notop.h5', THEANO_WEIGHTS_PATH_NO_TOP,
                                   cache_subdir='models')
        else:
            weights = get_file('vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5', TF_WEIGHTS_PATH_NO_TOP,
                                   cache_subdir='models')
        f = h5py.File(weights)

        layer_names = [name for name in f.attrs['layer_names']]

        if self.vgg_layers is None:
            self.vgg_layers = [layer for layer in model.layers
                               if 'vgg_' in layer.name]

        for i, layer in enumerate(self.vgg_layers):
            g = f[layer_names[i]]
            weights = [g[name] for name in g.attrs['weight_names']]
            layer.set_weights(weights)

        # Freeze all VGG layers
        for layer in self.vgg_layers:
            layer.trainable = False

        return model