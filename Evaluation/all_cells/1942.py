from tensorflow.contrib.learn.python.learn.utils import saved_model_export_utils
from tensorflow.contrib.learn.python.learn import learn_runner

PATTERN = "00001-of-"  # process only one of the shards, for testing purposes

def train_and_evaluate(output_dir):
    wide, deep = get_wide_deep()
    estimator = tf.estimator.DNNLinearCombinedRegressor(
                         model_dir=output_dir,
                         linear_feature_columns=wide,
                         dnn_feature_columns=deep,
                         dnn_hidden_units=[64, 32])
    train_spec=tf.estimator.TrainSpec(
                         input_fn=read_dataset('train', PATTERN),
                         max_steps=TRAIN_STEPS)
    exporter = tf.estimator.FinalExporter('exporter',serving_input_fn)
    eval_spec=tf.estimator.EvalSpec(
                         input_fn=read_dataset('eval', PATTERN),
                         steps=None,
                         exporters=exporter)
    tf.estimator.train_and_evaluate(estimator, train_spec, eval_spec)
    
shutil.rmtree('babyweight_trained', ignore_errors=True) # start fresh each time
train_and_evaluate('babyweight_trained')