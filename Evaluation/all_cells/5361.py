bbm = Model(name='b&b')
x, y, z = bbm.integer_var_list(3, name=['x', 'y', 'z'])
bbm.maximize(x + y + 2*z)
bbm.add_constraint(7*x + 2*y + 3*z <= 36)
bbm.add_constraint(5*x + 4*y + 7*z <= 42)
bbm.add_constraint(2*x + 3*y + 5*z <= 28)
bbm.solve(log_output=True);