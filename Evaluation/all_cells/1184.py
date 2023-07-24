ids_stable_period_1 = [];ids_stable_period_2=[];ids_stable_period_3=[];ids_no_stable_period=[]
for id in shop_info.index.tolist():
    if len(shop_info.loc[id,'stable_period_1'])>0:
        ids_stable_period_1.append(id)
    elif len(shop_info.loc[id,'stable_period_2'])>0:
        ids_stable_period_2.append(id)
    elif len(shop_info.loc[id,'stable_period_3'])>0:
        ids_stable_period_3.append(id)
    else:
        ids_no_stable_period.append(id)
print len(ids_stable_period_1),len(ids_stable_period_2),len(ids_stable_period_3),len(ids_no_stable_period)

# ids_stable_period_2
# ids_stable_period_3
# ids_no_stable_period