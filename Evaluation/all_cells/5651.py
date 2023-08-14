tags = (tag for i, (word, tag) in enumerate(data.training_set.stream()))
words = (word for i, (word, tag) in enumerate(data.training_set.stream()))
def pair_counts(sequences_A, sequences_B):
    """Return a dictionary keyed to each unique value in the first sequence list
    that counts the number of occurrences of the corresponding value from the
    second sequences list.
    
    For example, if sequences_A is tags and sequences_B is the corresponding
    words, then if 1244 sequences contain the word "time" tagged as a NOUN, then
    you should return a dictionary such that pair_counts[NOUN][time] == 1244
    """
    d1 = defaultdict(list)
    dict_word = defaultdict(list)
    for i , val in enumerate(zip(sequences_A, sequences_B)):
        d1[val[0]].append(val[1])

    for key, val in d1.items():
        dict_word[key] = Counter(val)

    return dict_word


# Calculate C(t_i, w_i)
emission_counts = pair_counts(tags, words)

print(len(emission_counts))
print(emission_counts['NOUN']['time'])
print(max(emission_counts["NOUN"], key=emission_counts["NOUN"].get))

assert len(emission_counts) == 12, \
       "Uh oh. There should be 12 tags in your dictionary."
assert max(emission_counts["NOUN"], key=emission_counts["NOUN"].get) == 'time', \
       "Hmmm...'time' is expected to be the most common NOUN."
HTML('<div class="alert alert-block alert-success">Your emission counts look good!</div>')