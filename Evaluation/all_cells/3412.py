try:
    print(y)
except(NameError) as err:
    print("NameError", err)
else:
    raise