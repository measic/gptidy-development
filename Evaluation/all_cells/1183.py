def cal_stable_period(x,base_sim):
    print x['shop_id']
    stable_period = []
    next_start_wk = 0
    for wk in range(0,66):
        if next_start_wk != 0 and wk != next_start_wk : 
            #print 'next_start_wk =',next_start_wk,'continue'
            continue
        #print wk
        next_start_wk = 0
        if x['cos_sim_wk_'+str(wk)] >  base_sim:
            #print x['shop_id'],'aa'
            for wknext in range(wk + 1,67):
                if x['cos_sim_wk_'+str(wknext)] > base_sim :
                    if wknext == 66:
                        stable_period.append([wk,wknext]) # wk~wknext(不包括wknext)
                        #print [wk,wknext]
                        next_start_wk = wknext
                        break
                    else:    
                        #print x['shop_id'],'bbbb'
                        pass
                else:
                    if wknext - wk >= 3 : 
                        stable_period.append([wk,wknext]) # wk~wknext(不包括wknext)
                        print [wk,wknext]
                        next_start_wk = wknext
                    else:
                        next_start_wk = 0
                    break #结束子循环
    #print 'id= ',x['shop_id'],stable_period
    return stable_period
shop_info['stable_period_1'] = shop_info.apply(lambda x: cal_stable_period(x,0.99),axis = 1)
shop_info['stable_period_2'] = shop_info.apply(lambda x: cal_stable_period(x,0.98),axis = 1)
shop_info['stable_period_3'] = shop_info.apply(lambda x: cal_stable_period(x,0.96),axis = 1)