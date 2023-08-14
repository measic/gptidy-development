x = pm.continuous_var(name='x')
y = pm.continuous_var(name='y')
pm.add_constraint(y == pwf2(x));  # y is constrained to be equal to f(x)