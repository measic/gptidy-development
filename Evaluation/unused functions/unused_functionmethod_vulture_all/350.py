import matplotlib.image as mpimg

def disp_image(img_path):
    img = mpimg.imread(img_path)
    fig = plt.figure()
    plt.subplot()
    plt.imshow(img)
    plt.axis('off')
    plt.plot()
    plt.show()