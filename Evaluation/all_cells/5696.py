import gensim, logging

model_path = 'GoogleNews-vectors-negative300.bin'
model = gensim.models.Word2Vec.load_word2vec_format(model_path, binary=True)