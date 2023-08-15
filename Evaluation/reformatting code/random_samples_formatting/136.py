try:
    point[0] = 20
except(TypeError) as er:
    print("TypeError:", er)
else:
    raise