print ("Total", "trues", "falses")
for sample in bag_clf1.estimators_samples_:
    count = 0
    trues = 0
    falses = 0
    for i in sample:
        count +=1
        if i:
            trues += 1
        else:
            falses += 1
    print ("%d\t%d\t%d\n" %(count, trues, falses))