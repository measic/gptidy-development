read_filename = './annotations_201712131226.csv'
import numpy as np
from scipy import stats

lista1 = []
lista2 = []
lista3 = []
with open(read_filename, 'r', newline='') as read, \
        open(read_filename+'.points', 'w', newline='') as write:
    reader = csv.reader(read)
    writer = csv.writer(write)
    for line in reader:
        #print(line)
        img = imageio.imread(line[0])
        lista1.append(estimate_anottation_correct(img, line[1:5], line_width=1))
        points = estimate_anottation_correct(img, line[1:5])
        lista2.append(points)
        lista3.append(estimate_anottation_correct(img, line[1:5], line_width=3))
        line.append(points)
        writer.writerow(line)
