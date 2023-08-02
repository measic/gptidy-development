import sys
import tarfile
from six.moves import urllib
TF_MODELS_URL = 'http://download.tensorflow.org/models'
INCEPTION_V3_URL = TF_MODELS_URL + '/inception_v3_2016_08_28.tar.gz'
INCEPTION_PATH = os.path.join('datasets', 'inception')
variable_def = os.path.join(INCEPTION_PATH, 'inception_v3.ckpt')

def download_progress(count, block_size, total_size):
    percent = count * block_size * 100 // total_size
    sys.stdout.write('\rDownloading: {}%'.format(percent))
    sys.stdout.flush()

def fetch_pretrained_inception_v3(url=INCEPTION_V3_URL, path=INCEPTION_PATH):
    if os.path.exists(variable_def):
        return
    os.makedirs(path, exist_ok=True)
    tgz_path = os.path.join(path, 'inception_v3.tgz')
    urllib.request.urlretrieve(url, tgz_path, reporthook=download_progress)
    inception_tgz = tarfile.open(tgz_path)
    inception_tgz.extractall(path=path)
    inception_tgz.close()
    os.remove(tgz_path)