def prepare_image_with_tensorflow(image, target_width=299, target_height=299, max_zoom=0.2):
    """Zooms and crops the image randomly for data augmentation."""
    image_shape = tf.cast(tf.shape(image), tf.float32)
    height = image_shape[0]
    width = image_shape[1]
    image_ratio = width / height
    target_image_ratio = target_width / target_height
    crop_vertically = image_ratio < target_image_ratio
    crop_width = tf.cond(crop_vertically, lambda: width, lambda: height * target_image_ratio)
    crop_height = tf.cond(crop_vertically, lambda: width / target_image_ratio, lambda: height)
    resize_factor = tf.random_uniform(shape=[], minval=1.0, maxval=1.0 + max_zoom)
    crop_width = tf.cast(crop_width / resize_factor, tf.int32)
    crop_height = tf.cast(crop_height / resize_factor, tf.int32)
    variable_def = tf.stack([crop_height, crop_width, 3])
    image = tf.random_crop(image, variable_def)
    image = tf.image.random_flip_left_right(image)
    image_batch = tf.expand_dims(image, 0)
    image_batch = tf.image.resize_bilinear(image_batch, [target_height, target_width])
    image = image_batch[0] / 255
    return image