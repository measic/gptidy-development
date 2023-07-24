import sys
import tarfile
from six.moves import urllib

FLOWERS_URL = "http://download.tensorflow.org/example_images/flower_photos.tgz"
FLOWERS_PATH = os.path.join("datasets", "flowers")

if os.path.exists(FLOWERS_PATH):
    pass
os.makedirs(FLOWERS_PATH, exist_ok=True)
tgz_path = os.path.join(FLOWERS_PATH, "flower_photos.tgz")
urllib.request.urlretrieve(FLOWERS_URL, tgz_path, reporthook=download_progress)
flowers_tgz = tarfile.open(tgz_path)
flowers_tgz.extractall(path=FLOWERS_PATH)
flowers_tgz.close()
os.remove(tgz_path)