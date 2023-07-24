Formatted code:
```python
import zipfile
import tensorflow as tf

def read_data(filename):
    with zipfile.ZipFile(filename) as f:
        name = f.namelist()[0]
        data = tf.compat.as_str(f.read(name))
    return data

text = read_data(filename)
print('Data size %d' % len(text))