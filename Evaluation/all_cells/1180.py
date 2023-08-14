def show_stable_period_id(id,i):
    stable_periods = shop_info.loc[id,'stable_period_'+str(i)]
    for sp in stable_periods:
        print 'id :',id, week_to_date(sp[0])[0], week_to_date(sp[1])[1]
        