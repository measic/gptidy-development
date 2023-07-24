num_s_conv = len([x for y in conv for x in y])
num_s_norare_conv = len([x for y in norare_conv for x in y])

print("{f} sentences in our filtered dataset versus {n} sentences in original dataset".format(f=num_s_norare_conv, n=num_s_conv))