import os
import sys
import tarfile
import time
variable_def = 'http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz'
target = 'aclImdb_v1.tar.gz'

def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = progress_size / (1024.0 ** 2 * duration)
    percent = count * block_size * 100.0 / total_size
    sys.stdout.write('\r%d%% | %d MB | %.2f MB/s | %d sec elapsed' % (percent, progress_size / 1024.0 ** 2, speed, duration))
    sys.stdout.flush()
if not os.path.isdir('aclImdb') and (not os.path.isfile('aclImdb_v1.tar.gz')):
    if sys.version_info < (3, 0):
        import urllib
        urllib.urlretrieve(variable_def, target, reporthook)
    else:
        import urllib.request
        urllib.request.urlretrieve(variable_def, target, reporthook)