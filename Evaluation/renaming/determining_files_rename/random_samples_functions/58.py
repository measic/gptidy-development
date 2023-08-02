path = untar_data(URLs.MNIST_SAMPLE)
data = ImageDataBunch.from_folder(path)

def function_def():
    return Learner(data, simple_cnn((3, 16, 16, 2)), metrics=[accuracy])
learn = function_def()