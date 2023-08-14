draws=[]
for i in range(1000):
    masses=np.random.normal(data4.mass,data4.mass_error_min)
    axes=np.random.normal(data4.semi_major_axis,data4.semi_major_axis_error_min)
    draws+=[(masses*axes).sum()/masses.sum()]