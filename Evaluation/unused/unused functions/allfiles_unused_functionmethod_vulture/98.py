def draw_rule_and_reg_id(id):
    plt.title(str(id))
    list_result = dateRange('2016-06-06','2016-10-31')
    for i in range(1,15):
        list_result.append('predict_day_'+str(i))
    xmajorLocator = MultipleLocator(7) #将x轴次刻度标签设置为7的倍数
    ax = plt.subplot(111) 
    ax.xaxis.set_major_locator(xmajorLocator)
    shop_info.loc[id ,list_result].T.plot(figsize=(16,9),ax=ax)
    

    list_result = dateRange('2016-06-06','2016-10-31')
    for i in range(1,8):
        list_result.append('predict_'+str(i))

    xmajorLocator = MultipleLocator(7) #将x轴次刻度标签设置为7的倍数
    ax = plt.subplot(111) 
    ax.xaxis.set_major_locator(xmajorLocator)
    shop_info.loc[id,list_result].T.plot(figsize=(16,9),ax=ax)
    plt.show()
