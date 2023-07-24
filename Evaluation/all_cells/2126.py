# This cell is not contained in the book but
# added for convenience so that the notebook
# can be executed starting here, without
# executing prior code in this notebook

import os
import gzip


if not os.path.isfile('movie_data.csv'):
    if not os.path.isfile('movie_data.csv.gz'):
        print('Please place a copy of the movie_data.csv.gz'
              'in this directory. You can obtain it by'
              'a) executing the code in the beginning of this'
              'notebook or b) by downloading it from GitHub:'
              'https://github.com/rasbt/python-machine-learning-'
              'book-2nd-edition/blob/master/code/ch08/movie_data.csv.gz')
    else:
        with in_f = gzip.open('movie_data.csv.gz', 'rb'), \
                out_f = open('movie_data.csv', 'wb'):
            out_f.write(in_f.read())