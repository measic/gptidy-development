'''Create the FP yield(A,Z) list container'''

cfpy_az = get_fpy_az( cfpy_az_df )

print('Sum of yield values in dictionary container = ',round(sum([fp.yield_percent for fp in cfpy_az]),2))
print('# of FP nuclides = ', len(cfpy_az))