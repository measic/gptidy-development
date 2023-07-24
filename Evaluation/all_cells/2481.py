brent_words = brent_x_train['word'].tolist()
provi_words = providence_x_train['word'].tolist()

difference = [w for w in brent_words if w not in provi_words]

print("%d words in Brent" %len(brent_words))
print("%d words in Providence" % len(provi_words))
print("Corpus coverage difference: ", difference)