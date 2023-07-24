#sess = tf.Session(config=tf.ConfigProto(device_count={'GPU': 0}))
sess = tf.Session()
dataset.run_initializers(sess)
sess.run(tf.global_variables_initializer())

merged_summary = tf.summary.merge_all()
writer = tf.summary.FileWriter(os.path.join(LOG_DIR, 's2s_sandbox', 'tmp'))
writer.add_graph(sess.graph)