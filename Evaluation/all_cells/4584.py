# Use a break statement to kill the loop
for n in range(10):
    if n > 5:
        print("n > 5")
        break
    else:
        print("n = %d" % n)