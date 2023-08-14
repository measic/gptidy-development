F=np.array(range(5,11))
#convert to a 2D matrix with 1 row and as many columns as the original size of F
F = F.reshape(1,F.size)
print(F)
# everything in columns 3, 4 and 5 of F. NOTE that using a colon in the list [] to specify the columns is not allowed.
F2 = F[:,[2,3,4]]
print(F2)
# here's another way to get the list specifying the columns
cols = range(2,5)
print(F[:,cols])