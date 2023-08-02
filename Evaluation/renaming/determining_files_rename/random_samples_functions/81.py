tags = [tag for i, (word, tag) in enumerate(data.training_set.stream())]
s = tags[:-1]
e = tags[1:]
spluse = list(zip(s, e))

def function_def(sequences):
    """Return a dictionary keyed to each unique PAIR of values in the input sequences
    list that counts the number of occurrences of pair in the sequences list. The input
    should be a 2-dimensional array.
    
    For example, if the pair of tags (NOUN, VERB) appear 61582 times, then you should
    return a dictionary such that your_bigram_counts[(NOUN, VERB)] == 61582
    """
    d4 = defaultdict(int)
    for i in sequences:
        d4[i] += 1
    return d4
tag_bigrams = function_def(spluse)
assert len(tag_bigrams) == 144, 'Uh oh. There should be 144 pairs of bigrams (12 tags x 12 tags)'
assert min(tag_bigrams, key=tag_bigrams.get) in [('X', 'NUM'), ('PRON', 'X')], "Hmmm...The least common bigram should be one of ('X', 'NUM') or ('PRON', 'X')."
assert max(tag_bigrams, key=tag_bigrams.get) in [('DET', 'NOUN')], "Hmmm...('DET', 'NOUN') is expected to be the most common bigram."
HTML('<div class="alert alert-block alert-success">Your tag bigrams look good!</div>')