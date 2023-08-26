def face_detector(img_path):
    variable_def = cv2.imread(img_path)
    gray = cv2.cvtColor(variable_def, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    return len(faces) > 0