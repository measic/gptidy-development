# variables for total production
desk = tm2.integer_var(name='desk', lb=100)
cell = tm2.continuous_var(name='cell', lb=100)

# two variables per machine type:
desk1 = tm2.integer_var(name='desk1')
cell1 = tm2.integer_var(name='cell1')

desk2 = tm2.integer_var(name='desk2')
cell2 = tm2.integer_var(name='cell2')

# yes no variable
z = tm2.binary_var(name='z')