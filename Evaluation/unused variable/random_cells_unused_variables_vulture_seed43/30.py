# turn into 1-d arrays, and only use values > 0 (sometimes no-value data is very large negative number)
array1 = array_1[array_1>0]
# array1 = array_1[array_1<100000000]
array2 = array_2[array_1>0]
# array2 = array_2[array_1<100000000]
array3 = array_3[array_1>0]
# array3 = array_3[array_1<100000000]