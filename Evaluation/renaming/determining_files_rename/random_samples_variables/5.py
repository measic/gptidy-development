import pyprind
import pandas as pd
import os
basepath = 'aclImdb'
labels = {'pos': 1, 'neg': 0}
variable_def = pyprind.ProgBar(50000)
df = pd.DataFrame()
for s in ('test', 'train'):
    for l in ('pos', 'neg'):
        path = os.path.join(basepath, s, l)
        for file in sorted(os.listdir(path)):
            with open(os.path.join(path, file), 'r', encoding='utf-8') as infile:
                txt = infile.read()
            df = df.append([[txt, labels[l]]], ignore_index=True)
            variable_def.update()
df.columns = ['review', 'sentiment']