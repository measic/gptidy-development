c_res, info = tneqsys.solve([1]*5, np.array(c0+K))
c0, c_res, info['success']