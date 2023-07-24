u1_z = lpf.lpfilter(df['u1_z']/100, 50)   #大腿角速度z成分
u2_z = lpf.lpfilter(df['u2_z']/100, 50)   #下腿角速度z成分