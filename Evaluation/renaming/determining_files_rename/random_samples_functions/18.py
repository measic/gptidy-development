def function_def(sequences):
    """Return a dictionary keyed to each unique value in the input sequences list
    that counts the number of occurrences where that value is at the beginning of
    a sequence.
    
    For example, if 8093 sequences start with NOUN, then you should return a
    dictionary such that your_starting_counts[NOUN] == 8093
    """
    d4 = defaultdict(int)
    for i in sequences:
        d4[i[0]] += 1
    return d4
tag_starts = function_def(data.training_set.Y)
print(tag_starts)
assert len(tag_starts) == 12, 'Uh oh. There should be 12 tags in your dictionary.'
assert min(tag_starts, key=tag_starts.get) == 'X', "Hmmm...'X' is expected to be the least common starting bigram."
assert max(tag_starts, key=tag_starts.get) == 'DET', "Hmmm...'DET' is expected to be the most common starting bigram."
HTML('<div class="alert alert-block alert-success">Your starting tag counts look good!</div>')