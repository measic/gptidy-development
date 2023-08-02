data = data_ep[pd.notnull(data_ep["mass"])]
data = data[pd.notnull(data["semi_major_axis"])]
data1 = data[['star_name','mass','semi_major_axis']]

Data1=System(data1)
#Data1.M_total
#Data1 = pd.DataFrame({'system_name':Data1.system,'total_mass':Data1.M_total.tolist(),'center_of_Mass':Data1.CM.tolist()})
#data1
#problema que guarda total mass en la funcion 