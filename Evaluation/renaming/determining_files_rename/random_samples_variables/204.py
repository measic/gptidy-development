import csv
import datetime
import os
import glob
IMG_PATH = '/home/ivan/Área de trabalho/2017'
variable_def = []
for filename in glob.iglob(IMG_PATH + '**/*/*/*/*stamp.jpg*', recursive=True):
    variable_def.append(filename)
print(variable_def[:4])
print(len(variable_def))
print(find_conteiner(variable_def[1]))
print(find_conteiner(variable_def[15]))