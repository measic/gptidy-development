def function_def(img_path):
    prediction = ResNet50_predict_labels(img_path)
    return (prediction <= 268) & (prediction >= 151)