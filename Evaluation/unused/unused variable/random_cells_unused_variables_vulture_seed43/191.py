basic_model = HiddenMarkovModel(name="base-hmm-tagger")

tags = (tag for i, (word, tag) in enumerate(data.training_set.stream()))
words = (word for i, (word, tag) in enumerate(data.training_set.stream()))

# TODO: create states with emission probability distributions P(word | tag) and add to the model
# (Hint: you may need to loop & create/add new states)
#basic_model.add_states()

emission_counts = pair_counts(tags, words)
states = {}
for tag, word_dict in emission_counts.items():
    emission_dict = defaultdict(float)
    for word in word_dict.keys():
        emission_dict[word] = emission_counts[tag][word] / tag_unigrams[tag] 
    state_emission = DiscreteDistribution(dict(emission_dict))
    states[tag] = State(state_emission, name=tag)
    
basic_model.add_states(list(states.values()))

# TODO: add edges between states for the observed transition frequencies P(tag_i | tag_i-1)
# (Hint: you may need to loop & add transitions
#basic_model.add_transition()
for tag in data.training_set.tagset:
    state = states[tag]
    basic_model.add_transition(basic_model.start, state, tag_starts[tag]/len(data.training_set))
    basic_model.add_transition(state, basic_model.end, tag_ends[tag]/tag_unigrams[tag])
    for next_tag in data.training_set.tagset:
        next_state = states[next_tag]
        basic_model.add_transition(state, next_state, tag_bigrams[(tag, next_tag)]/tag_unigrams[tag])

# NOTE: YOU SHOULD NOT NEED TO MODIFY ANYTHING BELOW THIS LINE
# finalize the model
basic_model.bake()

assert all(tag in set(s.name for s in basic_model.states) for tag in data.training_set.tagset), \
       "Every state in your network should use the name of the associated tag, which must be one of the training set tags."
assert basic_model.edge_count() == 168, \
       ("Your network should have an edge from the start node to each state, one edge between every " +
        "pair of tags (states), and an edge from each state to the end node.")
HTML('<div class="alert alert-block alert-success">Your HMM network topology looks good!</div>')