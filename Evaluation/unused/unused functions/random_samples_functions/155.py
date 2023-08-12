### TODO: Write a function that takes a path to an image as input
### and returns the dog breed that is predicted by the model.

from keras.applications.inception_v3 import InceptionV3
from keras.applications.inception_v3 import preprocess_input as preprocess_inception_input

def detect_dog_breed(img_path, given_model, use_bottleneck=True, img_H=224, img_W=224):
    ''' Detect dog breed given image in the img_path,
        using given model, using either bottleneck features (or not)
        with given img Height and Width
        
        @return: Dog breed (str)
    '''
    print('Detecting dog breed...')
    tensor = path_to_tensor(img_path, img_H, img_W)
    
    # using given image, extract its bottleneck features by running thru InceptionV3 n/w first
    if use_bottleneck: 
        tensor = extract_InceptionV3(tensor)
    else:
        tensor = preprocess_inception_input(tensor)
    
    # print('  [input tensor shape: {}]'.format(tensor.shape))
    # make predictions (probabilities)
    predicted_vector = given_model.predict(tensor)
    # get max index
    y_hat = np.argmax(predicted_vector)
    chance = 100. * predicted_vector[0][y_hat]  # probability of correctness
    # print('  [y_hat:{}]'.format(y_hat))
    # print('  prob:{:.2f}%'.format(chance))

    # return dog breed and probability 
    return dog_names[y_hat], chance