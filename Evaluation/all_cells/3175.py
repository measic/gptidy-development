'''Generate a list of nuclides with 1% or more fission yield'''

fp_1_percent = list() # this list will be used later

for fp in cfpy_az:
    if fp.yield_percent >= 1.0:
        fp_1_percent.append(fp)
        
print('# of FP nuclides = ', len(fp_1_percent))