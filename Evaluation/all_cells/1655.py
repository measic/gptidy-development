period    = 200
power_data_250 = np.ndarray((len(range(period,len(volt_data),period))*5,1))
start = np.argmin(volt_data[0:200])

i=0
for j in range(start,len(power_data),period):
    power_data_250[i:i+5] = np.mean(power_data[j:j+period])
    i += 5

#Linear interpolation instead of constant value upsampling
i=0
lin_in=np.ndarray((5,1))
for j in range(0,len(power_data_250),5):
    a = power_data_250[i]
    if i+6 > len(power_data_250):
        break
    b = power_data_250[i+6]
    lin_in = np.linspace(a,b,num=5).reshape(5,1)
    power_data_250[i:i+5] = lin_in
    i+=5