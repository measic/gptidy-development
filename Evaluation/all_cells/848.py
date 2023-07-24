for i in range(len(nlist)):
    data4=data3[data3.star_name==nlist[i]]
    draws=[]
    for i in range(1000):
        masses=np.random.normal(data4.mass,data4.mass_error_min)
        axes=np.random.normal(data4.semi_major_axis,data4.semi_major_axis_error_min)
        draws+=[(masses*axes).sum()/masses.sum()]
    mtot=(data4.mass).sum()
    com=(data4.mass*data4.semi_major_axis).sum()/mtot
    dcmdmi=(data4.semi_major_axis-com)/mtot
    dcmdri=data4.mass/mtot
    erd=np.std(draws)
    erp=np.sqrt((dcmdmi**2*data4.mass_error_min**2+dcmdri**2*data4.semi_major_axis_error_min**2).sum())
    print(np.median(draws),erd,erp)