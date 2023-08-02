DEBUG = False
JPEG_EXTENSIONS = ('.jpeg', '.JPEG', '.jpg', '.JPG')
image_dir = '../data/images'
test_images_dir = '../data/test_images'
stored_images_resized = '../data/images_resized'
stored_bottlenecks = '../data/bottlenecks'
tmp_dir = '/tmp'
bottleneck_dir = os.path.join(tmp_dir, 'bottlenecks')
variable_def = os.path.join(tmp_dir, 'images_resized')
summaries_dir = os.path.join(tmp_dir, 'retrain_logs')
model_dir = os.path.join(tmp_dir, 'inception')
inception_url = 'http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz'
output_graph_orig = 'output_graph_orig.pb'
output_graph = 'output_graph.pb'
output_labels = 'output_labels.txt'
architecture = 'inception_v3'
final_tensor_name = 'final_result'
how_many_training_steps = 500
learning_rate = 0.01
testing_percentage = 10
validation_percentage = 10
eval_step_interval = 10
train_batch_size = 100
test_batch_size = -1
validation_batch_size = 100
print_misclassified_test_images = False
flip_left_right = False
random_crop = 0
random_scale = 0
random_brightness = 0
force_inception_download = False
FLAGS = type('FlagsObject', (object,), {'architecture': architecture, 'model_dir': model_dir, 'intermediate_store_frequency': 0, 'summaries_dir': summaries_dir, 'learning_rate': learning_rate, 'image_dir': variable_def, 'testing_percentage': testing_percentage, 'validation_percentage': validation_percentage, 'random_scale': random_scale, 'random_crop': random_crop, 'flip_left_right': flip_left_right, 'random_brightness': random_brightness, 'bottleneck_dir': bottleneck_dir, 'final_tensor_name': final_tensor_name, 'how_many_training_steps': how_many_training_steps, 'train_batch_size': train_batch_size, 'test_batch_size': test_batch_size, 'eval_step_interval': eval_step_interval, 'validation_batch_size': validation_batch_size, 'print_misclassified_test_images': print_misclassified_test_images, 'output_graph': output_graph, 'output_labels': output_labels})
retrain.FLAGS = FLAGS