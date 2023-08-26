import numpy as np

def word2embedding(sent, i):
    word = sent[i][0]
    postag = sent[i][1]
            
    if word in model.vocab:
        worde = word
    else:
        worde = 'null'
    
    res = model[worde]
     
    if i > 0:
        word1 = sent[i-1][0]
        if word1 in model.vocab:
            worde = word1
        else:
            worde = 'null'
    
        res.extend(model[worde])
    
    else:
        res.extend(model['null'])
  
        
    if i < len(sent)-1:
        word1 = sent[i+1][0]
        if word1 in model.vocab:
            worde = word1
        else:
            worde = 'null'
        res.extend(model[worde])
    
    else:
        res.extend(model['null'])
    
    res.shape = (1,900)
    return res
        
def sent2embedding(sent):
        rese = []
        for  i in range(len(sent)):
            line = word2embedding(sent,i)
            rese.append(line)
        
        resee = np.vstack(rese)
                #rese.extend(word2embedding(sent, i))
        #print(resee.shape)
        return resee