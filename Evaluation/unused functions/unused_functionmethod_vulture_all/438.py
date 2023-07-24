# Get standard deviation of the normal distribution we use for weights initialization 
# of convolution and fully connected layers

def get_conv_bounds(input_feature_map, output_feature_map, filter_height, filter_width):
    fan_in = input_feature_map * filter_height * filter_width 
    fan_out = output_feature_map * filter_height * filter_width

    W_bound = np.sqrt(2. / (fan_in + fan_out))
    
    return W_bound

def get_fc_bounds(input_feature_map, output_feature_map):
    W_bound = np.sqrt(2. / (input_feature_map + output_feature_map))
    return W_bound


def create_conv_weight(input_feature_map, output_feature_map, filter_height, filter_width, weight_name):
    W_bound = get_conv_bounds(input_feature_map, output_feature_map, filter_height, filter_height)
    return tf.Variable(tf.truncated_normal(
            [filter_height, filter_width, input_feature_map, output_feature_map], stddev=W_bound), name=weight_name)


def create_fc_weight(input_feature_map, output_feature_map, weight_name):
    W_bound = get_fc_bounds(input_feature_map, output_feature_map)
    return tf.Variable(tf.truncated_normal(
        [input_feature_map, output_feature_map], stddev=W_bound), name=weight_name)