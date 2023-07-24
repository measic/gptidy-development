wordcount={}
no_of_words = 0
no_of_chars = 0
step = 0
total = len(data['text'])
increment = total//40

for x in data['text']:
    if((step % increment) == 0):
        sys.stdout.write(".")
        sys.stdout.flush()
    #s = "I am going to disco and bar tonight"
    step += 1
    tokens = cleanupDoc(x)
    for token in tokens:
        if token not in wordcount:
            wordcount[token] = 1
            no_of_words +=1
            no_of_chars += len(token)
        else:
            wordcount[token] += 1
            no_of_words +=1
            no_of_chars += len(token)
    

print("\n")
print("number of characters in labelled documents: ",no_of_chars)
print("number of words in labelled documents: ",no_of_words)
print("number of different words in labelled docs ",len(wordcount))    