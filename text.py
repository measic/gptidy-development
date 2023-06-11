if kwargs:
        for key in kwargs:
            if not (has_arg(tf.Session.run, key, True) or has_arg(Function.__init__, key, True)):
                msg = 'Invalid argument "%s" passed to K.function with TensorFlow backend' % key
                raise ValueError(msg)