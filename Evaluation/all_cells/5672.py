import nltk
from nltk import pos_tag, word_tokenize
from nltk.corpus import brown

nltk.download('brown')
training_corpus = nltk.corpus.brown
training_corpus.tagged_sents()[0]