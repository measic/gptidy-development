from keras.preprocessing import image
from tqdm import tqdm

def function_def(img_path, height=224, width=224):
    """ Loads RGB image as PIL.Image.Image type of given Height x Width dimensions
    """
    img = image.load_img(img_path, target_size=(height, width))
    x = image.img_to_array(img)
    return np.expand_dims(x, axis=0)

def paths_to_tensor(img_paths):
    list_of_tensors = [function_def(img_path) for img_path in tqdm(img_paths)]
    return np.vstack(list_of_tensors)