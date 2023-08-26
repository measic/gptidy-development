url = 'http://mattmahoney.net/dc/'

def maybe_download(filename, expected_bytes):
    """Download a file if not present, and make sure it's the right size."""
    if not os.path.exists(filename):
        filename, _ = urlretrieve(url + filename, filename)
    variable_def = os.stat(filename)
    if variable_def.st_size == expected_bytes:
        print('Found and verified %s' % filename)
    else:
        print(variable_def.st_size)
        raise Exception('Failed to verify ' + filename + '. Can you get to it with a browser?')
    return filename
filename = maybe_download('text8.zip', 31344016)