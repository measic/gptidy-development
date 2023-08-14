password = input("Please choose a password with at least 7 characters: ")
if len(password) < 7:
    raise Exception("This password is not long enough")