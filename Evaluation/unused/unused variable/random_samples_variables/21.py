import pandas as pd
read_filename = './annotations_201712131226.csv'

df = pd.read_csv(read_filename+'.points', names=('filename', 'x1', 'y1', 'x2', 'y2', 'points'))