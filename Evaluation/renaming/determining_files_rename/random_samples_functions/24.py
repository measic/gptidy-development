import sys
import tarfile
from six.moves import urllib
FLOWERS_URL = 'http://download.tensorflow.org/example_images/flower_photos.tgz'
FLOWERS_PATH = os.path.join('datasets', 'flowers')

def function_def(url=FLOWERS_URL, path=FLOWERS_PATH):
    if os.path.exists(FLOWERS_PATH):
        return
    os.makedirs(path, exist_ok=True)
    tgz_path = os.path.join(path, 'flower_photos.tgz')
    urllib.request.urlretrieve(url, tgz_path, reporthook=download_progress)
    flowers_tgz = tarfile.open(tgz_path)
    flowers_tgz.extractall(path=path)
    flowers_tgz.close()
    os.remove(tgz_path)