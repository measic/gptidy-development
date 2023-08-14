spent = []
#일부
for i in range(1,3):
#전체
#for i in range(len(corpora)):
    start = time.time()
    model = Word2Vec(corpora[i], **params_tag[i])
    spent.append('Elapsed time: '+str(time.time() - start)+' sec'+' ['+name_model[i]+']')
    model.wv.save(name_model[i])
print(spent)