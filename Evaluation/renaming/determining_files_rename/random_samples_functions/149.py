from keras.applications.resnet50 import preprocess_input, decode_predictions

def function_def(img_path):
    img = preprocess_input(path_to_tensor(img_path))
    return np.argmax(ResNet50_model.predict(img))