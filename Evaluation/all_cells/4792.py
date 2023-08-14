import zipfile
from urllib import request
import os, sys

path_coco = r"http://images.cocodataset.org/zips/train2014.zip"
filename="train2014"
def _progress(count, block_size, total_size):
            sys.stdout.write('\rDownloading %s %.2f%%' % (filename,
                float(count * block_size) / float(total_size) * 100.0))
            sys.stdout.flush()

if not os.path.exists("tests\coco"):
    print("Downloading Coco images")
    filehandler, _ = request.urlretrieve(path_coco, reporthook=_progress)
    zf = zipfile.ZipFile(filehandler)
    uncompress_size = sum((file.file_size for file in zf.infolist()))

    extracted_size = 0
    print()
    print("Extracting images")

    for file in zf.infolist():
        extracted_size += file.file_size
        sys.stdout.write('\rExtracting %.2f%%' % (float(extracted_size * 100/uncompress_size)))
        sys.stdout.flush()
        zf.extract(file, "tests/coco")

    os.rename("tests/coco/train2014", "tests/coco/images")

    filename="annotations"
    path_cocoann = r"http://images.cocodataset.org/annotations/annotations_trainval2014.zip"

    print("\nDownloading Coco annotations")
    filehandler, _ = request.urlretrieve(path_cocoann, reporthook=_progress)

    zf = zipfile.ZipFile(filehandler)
    print()
    print("Extracting annotations")
    uncompress_size = sum((file.file_size for file in zf.infolist()))

    extracted_size = 0

    for file in zf.infolist():
        extracted_size += file.file_size
        sys.stdout.write('\rExtracting %.2f%%' % (float(extracted_size * 100/uncompress_size)))
        sys.stdout.flush()
        zf.extract(file, "tests/coco")
print()
print("Coco is all set!!")