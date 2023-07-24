#counter.emission_counts - count per word,ne_tag
#counter.ngram_counts - count per ne_tag, ne_tag, ne_tag
# Initialize a trigram counter
counter = Hmm(3)
# Collect counts
counter.train()
# calc e
## should replace with Lidstone estimator
counter.calc_count_xy_y()
# calc q
counter.calc_transition_count()