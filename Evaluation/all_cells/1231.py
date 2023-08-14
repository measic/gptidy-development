for id in shop_info.index.tolist():
    for i in range(1,15):
        if shop_info.loc[id,'predict_day_'+str(i)] <0:
            print 'ERROR'