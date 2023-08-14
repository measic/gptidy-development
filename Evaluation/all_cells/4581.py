# use continue in a loop to skip the rest of the code in that given iteration
numbers = [1, 2, 3, 4.0, 5, 6, 7.0, 8]
for n in numbers:
    if type(n) != int:
        continue
    print("The number %s is an integer" % n)