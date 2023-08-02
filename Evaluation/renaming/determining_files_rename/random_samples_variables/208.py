if use_toy_data:
    input_fn = 'toy_input.txt'
    with open(input_fn, 'w') as f:
        f.write('a b c\td e f d e f\n')
        f.write('d e f\ta b c a b c\n')
else:
    DATA_DIR = '../../data/'
    input_fn = 'instrumental.full.train'
    input_fn = os.path.join(DATA_DIR, input_fn)
    if not os.path.exists(input_fn):
        import urllib
        variable_def = urllib.request.URLopener()
        variable_def.retrieve('http://sandbox.mokk.bme.hu/~judit/resources/instrumental.full.train', input_fn)