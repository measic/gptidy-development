import zipfile
from urllib import request

path_set5 = r"https://github.com/titu1994/Super-Resolution-using-Generative-Adversarial-Networks/releases/download/v0.1/Set5.zip"
filename="Set5"
def _progress(count, block_size, total_size):
            sys.stdout.write('\rDownloading %s %.2f%%' % (filename,
                float(count * block_size) / float(total_size) * 100.0))
            sys.stdout.flush()

if not os.path.exists("tests/set5/set5"):
    print("Downloading Set5 images")
    filehandler, _ = request.urlretrieve(path_set5, reporthook=_progress)
    zf = zipfile.ZipFile(filehandler)
    print()
    print("Extracting images")
    uncompress_size = sum((file.file_size for file in zf.infolist()))

    extracted_size = 0

    for file in zf.infolist():
        extracted_size += file.file_size
        sys.stdout.write('\rExtracting %.2f%%' % (float(extracted_size * 100/uncompress_size)))
        sys.stdout.flush()
        zf.extract(file, "tests/set5")
    
print()
print("Set5 is all set!!")