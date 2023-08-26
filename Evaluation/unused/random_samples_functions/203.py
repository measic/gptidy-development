### TODO: Write your algorithm.
### Feel free to use as many code cells as needed.

def whose_a_good_doggy(img_path):
    ''' Using the given image (in img_path), returns either:
        - Dog breed (if it's a dog)
        - Dog breed that resembles a human (if it's a human face)
        
        Uses the transfer-learned CNN model from Step 5
    '''
    print('.'*60)
    print('Given image:', img_path)
    
    # human face?
    human_found = face_detector(img_path)
    print('Found human:', human_found)
    
    # doggy ?
    # dog_found   = dog_detector(img_path)
    # print('Found dog:  ', dog_found)
    
    # find breed of dog
    breed, chance = detect_dog_breed(img_path, inception_bneck, use_bottleneck=True, img_H=229, img_W=229)
    print()
    print('Image is dog breed: {} ({:.2f}% prob)'.format(breed, chance))
    print('🐶 Woof!') if not human_found else print('Hellooo, 🐱👩🏻👦🏻👧🏻 animal 🤔')
    print('='*60)