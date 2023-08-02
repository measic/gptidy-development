def function_def(filename):
    with zipfile.ZipFile(filename) as f:
        name = f.namelist()[0]
        data = tf.compat.as_str(f.read(name))
    return data
text = function_def(filename)
print('Data size %d' % len(text))