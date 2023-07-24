import sys
import tarfile
from six.moves import urllib

TF_MODELS_URL = "http://download.tensorflow.org/models"
INCEPTION_V3_URL = TF_MODELS_URL + "/inception_v3_2016_08_28.tar.gz"
INCEPTION_PATH = os.path.join("datasets", "inception")
INCEPTION_V3_CHECKPOINT_PATH = os.path.join(INCEPTION_PATH, "inception_v3.ckpt")

if os.path.exists(INCEPTION_V3_CHECKPOINT_PATH):
    pass
os.makedirs(path, exist_ok=True)
tgz_path = os.path.join(path, "inception_v3.tgz")
urllib.request.urlretrieve(url, tgz_path, reporthook=download_progress)
inception_tgz = tarfile.open(tgz_path)
inception_tgz.extractall(path=path)
inception_tgz.close()
os.remove(tgz_path)