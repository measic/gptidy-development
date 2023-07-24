print("yielded accuracy:")

for r_unit in r_units:
    
    print(r_unit, np.max(logs[r_unit]["val_acc"]))