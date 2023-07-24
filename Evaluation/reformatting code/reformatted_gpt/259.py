try:
    raise Exception("description of the error")
except Exception as err:
    print("Exception:", err)