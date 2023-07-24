import nltk
from nltk.corpus import stopwords
import sys

def cleanupDoc(s):
     stopset = set(stopwords.words('english'))
     tokens = nltk.word_tokenize(s)
     cleanup = [token.lower() for token in tokens if token.lower() not in stopset and  len(token)>2]
     return cleanup