def face_detector(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    variable_def = face_cascade.detectMultiScale(gray)
    return len(variable_def) > 0