def function_def(img_path, cascade):
    """ Alternate implementation of Face Detector - using given Haar Cascade file
        :img_path - path to image file
        :cascade - cascade algo to use
        :returns - True if face found, else False
    """
    img = cv2.imread(img_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(img_gray)
    return len(faces) > 0