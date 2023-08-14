from filterpy.kalman import update
z = 1.
x, P = update(x, P, z, R, H)
print('x =', x)