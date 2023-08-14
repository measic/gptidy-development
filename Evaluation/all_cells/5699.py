Xe = []
for s in train_sents:
        mat = sent2embedding(s)
        Xe.append(mat)
Xee = np.vstack(Xe)
finalX = np.concatanate(X,Xee)


Xet = []
for s in test_sents:
        mat = sent2embedding(s)
        Xet.append(mat)
Xeet = np.vstack(Xet)
finalXt = np.concatanate(Xt,Xeet)