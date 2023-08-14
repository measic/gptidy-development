#test
corpus = corpora[0]
print('corpus 길이', len(corpus))
total = pd.DataFrame([len(sent) for sent in corpus]).sum()
length = 0
for line in corpus:
    length = max(length, len(line))
print('corpus내 최대 길이', length)
print('corpus내 모든 장소 합', total)