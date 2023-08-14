sample = samples[0x1][0]
print(sample)
print(check_touchcode(sample))
print(check_touchcode(samples[0x10][1]))
print(check_touchcode(None))
print(check_touchcode_str("[(0,0),(0,3),(3,0),(2,3),(1,3)]", x_mirror=False))
print(check_touchcode_str("+++A LOT OF GARGABE+++"))
