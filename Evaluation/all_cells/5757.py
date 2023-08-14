os.listdir("new-traffic-signs/")
repo = "new-traffic-signs/"
X = []
for image_locations in os.listdir(repo):
    if image_locations != '.DS_Store':
        img = mpimg.imread(repo+image_locations)
        img_resized = cv2.resize(img,(image_size,image_size), interpolation = cv2.INTER_AREA)
        X.append(img_resized)
    
X2 = np.stack(X, axis = 0)
X2 = X2.astype(np.uint8)

num_own_examples = len(X2)
