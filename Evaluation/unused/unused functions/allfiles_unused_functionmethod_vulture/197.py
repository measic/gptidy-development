def get_rhymes(words):
    num_words = len(words)
    rhymes = np.empty((num_words, num_words))
    
    for i in range(num_words):
        for j in (k for k in range(num_words) if not k == i):
            if poetrytools.rhymes(words[i], words[j]):
                rhymes[i][j] = 1
    return rhymes