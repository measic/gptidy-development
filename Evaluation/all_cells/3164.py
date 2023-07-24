'''Compute half-life times of cumulative FP with >0.1% yield'''

fp_0dot1_percent = list()

for fp in cfpy_az:
    if fp.yield_percent >= 0.1:
        fp_0dot1_percent.append(fp)
        
print('total # of FP nuclides = ', len(fp_0dot1_percent))
print('')

half_life_times( fp_0dot1_percent, nuclides )