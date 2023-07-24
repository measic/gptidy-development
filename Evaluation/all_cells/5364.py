
# total production is sum of type1 + type 2
tm2.add_constraint(desk == desk1 + desk2)
tm2.add_constraint(cell == cell1 + cell2)

# production on assembly machine of type 1 must be less than 400 if z is 1, else 0
tm2.add_constraint(0.2 * desk1 + 0.4 * cell1 <= 400 * z)
# production on assembly machine of type 2 must be less than 430 if z is 0, else 0
tm2.add_constraint(0.25 * desk2 + 0.3 * cell2 <= 430 * (1-z))

# painting machine limit is identical
# constraint #4: painting time limit
tm2.add_constraint( 0.5 * desk + 0.4 * cell <= 490)

tm2.print_information()