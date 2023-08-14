for _ in range(4):
    x, P = predict(x=x, P=P, F=F, Q=0)
    print('x =', x)