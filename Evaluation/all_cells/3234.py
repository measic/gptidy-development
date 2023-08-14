# Set DEBUG to True for more output
DEBUG = False

# Expect image files to always end with one of these
JPEG_EXTENSIONS = ('.jpeg', '.JPEG', '.jpg', '.JPG')

# Raw input images come from this dir in the git repo (or you can customize this to point to a new dir).
# Only JPEG images are used. We will resize these images before using them.
image_dir = '../data/images'

# We kept some images separate for our manual testing at the end.
test_images_dir = '../data/test_images'

# If stored_images_resized, images here have already been resized are can be used w/o re-resizing
stored_images_resized = '../data/images_resized'  # set to None to ignore

# If stored_bottlenecks, supplement the image_dir collection with persisted bottlenecks from this dir
stored_bottlenecks = '../data/bottlenecks'  # set to None to ignore

# Working files are in /tmp by default
tmp_dir = '/tmp'
bottleneck_dir = os.path.join(tmp_dir, 'bottlenecks')
images_resized_dir = os.path.join(tmp_dir, 'images_resized')
summaries_dir = os.path.join(tmp_dir, 'retrain_logs')

# Download the original inception model to/from here
model_dir = os.path.join(tmp_dir, 'inception')
inception_url = 'http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz'

# Store the graph before and after training
output_graph_orig = "output_graph_orig.pb"
output_graph = "output_graph.pb"
output_labels = "output_labels.txt"

# Training params
architecture = 'inception_v3'
final_tensor_name = "final_result"
how_many_training_steps = 500
learning_rate = 0.01
testing_percentage = 10
validation_percentage = 10
eval_step_interval = 10
train_batch_size = 100
test_batch_size = -1
validation_batch_size = 100
print_misclassified_test_images = False

# Since we are using persisted bottleneck files, we won't play with distortion.
# Distortion would have limited impact with our small set of image files.
flip_left_right = False
random_crop = 0
random_scale = 0
random_brightness = 0

# Download once and re-use by default
force_inception_download = False

# Create a FLAGS object with these attributes
FLAGS = type('FlagsObject', (object,), {
    'architecture': architecture,
    'model_dir': model_dir,
    'intermediate_store_frequency': 0,
    'summaries_dir': summaries_dir,
    'learning_rate': learning_rate,
    'image_dir': images_resized_dir,
    'testing_percentage': testing_percentage,
    'validation_percentage': validation_percentage,
    'random_scale': random_scale,
    'random_crop': random_crop,
    'flip_left_right': flip_left_right,
    'random_brightness': random_brightness,
    'bottleneck_dir': bottleneck_dir,
    'final_tensor_name': final_tensor_name,
    'how_many_training_steps': how_many_training_steps,
    'train_batch_size': train_batch_size,
    'test_batch_size': test_batch_size,
    'eval_step_interval': eval_step_interval,
    'validation_batch_size': validation_batch_size,
    'print_misclassified_test_images': print_misclassified_test_images,
    'output_graph': output_graph,
    'output_labels': output_labels
})

# Setting the FLAGS in retrain allows us to call the functions directly
retrain.FLAGS = FLAGS