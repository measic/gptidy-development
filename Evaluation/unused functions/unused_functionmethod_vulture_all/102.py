def qda_accracy():
    c1_result = [] 
    c2_result = []
    miss = []
    
    for i in c1.test:
        c1_result.append(qda(i)<0)
        if qda(i)>0:
            miss.append(i)
    
    for i in c2.test:
        c2_result.append(qda(i)>0)
        if qda(i)<0:
            miss.append(i)
    
    miss = np.array(miss)
    acc = (sum(c1_result) + sum(c2_result))/200
    
    return acc, miss