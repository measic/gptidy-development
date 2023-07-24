from collections import OrderedDict
num_imgs = len(df)

bboxes = np.zeros((num_imgs, 4))
imgs = OrderedDict()
for index, row in df.iterrows():
    im = imageio.imread(row['filename'])[:,:,0]
    #bboxe
    imgs[index] = (im, os.path.basename(os.path.split(row['filename'])[0]))
    bboxes[index] = [row['x1'], row['y1'], row['x2'], row['y2']]
