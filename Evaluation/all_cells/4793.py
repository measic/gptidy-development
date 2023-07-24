import zipfile
from urllib import request

path_bsd100 = r"https://github.com/titu1994/Super-Resolution-using-Generative-Adversarial-Networks/releases/download/v0.1/bsd100.zip"
filename="bsd100.zip"
def _progress(count, block_size, total_size):
            sys.stdout.write('\rDownloading %s %.2f%%' % (filename,
                float(count * block_size) / float(total_size) * 100.0))
            sys.stdout.flush()

if not os.path.exists("tests/bsd100/bsd100"):
    print("Downloading BSD100 images")
    filehandler, _ = request.urlretrieve(path_bsd100, reporthook=_progress)
    zf = zipfile.ZipFile(filehandler)
    print()

    print("Extracting images")
    uncompress_size = sum((file.file_size for file in zf.infolist()))

    extracted_size = 0

    for file in zf.infolist():
        extracted_size += file.file_size
        sys.stdout.write('\rExtracting %.2f%%' % (float(extracted_size * 100/uncompress_size)))
        sys.stdout.flush()
        zf.extract(file, "tests/bsd100")
print()
print("BSD100 is all set")