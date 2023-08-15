'''Total sum of independent FP yield per 100 fissions'''

print('Total sum = ',round(sum([fpy.yield_percent for fpy in cfpy_az]),1))