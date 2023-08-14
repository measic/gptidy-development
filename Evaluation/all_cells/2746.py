def generate_line(model, words, seed=None, rhymes=None):
    syllables_left = 10
    last_stress = 0
    
    line= []
    start_probs = model.startprob_
    emission_probs = model.emissionprob_
    transition_probs = model.transmat_
    
    start_state = np.random.choice(len(start_probs), p = start_probs)
    
    if seed is not None:
        possible_start_emissions = np.where(rhymes[seed] == 1)
        probs = np.array(emission_probs[start_state][possible_start_emissions])

        scaled_probs = probs / sum(probs)
        while True:
            start_emission = np.random.choice(possible_start_emissions[0], p=scaled_probs)
            start_stress = poetrytools.stress(words[start_emission])
            if len(start_stress) == 1 or int(start_stress[-1]) == 1 :
                break
    else:
        while True:
            start_emission = np.random.choice(len(emission_probs[start_state]), p=emission_probs[start_state])
            start_stress = poetrytools.stress(words[start_emission])
            if len(start_stress) == 1 or int(start_stress[-1]) == 1:
                break
    
    line.append(start_emission)
    start_stress = poetrytools.stress(words[start_emission])
    syllables_left -= len(start_stress)
    
    if len(start_stress) == 1:
        prev_starting_stress = 1
    else:
        prev_starting_stress = int(start_stress[0])

    curr_state = start_state
    while syllables_left > 0:
        possible_transitions = transition_probs[curr_state]
        curr_state = np.random.choice(len(possible_transitions), p=possible_transitions)
        possible_emissions = emission_probs[curr_state]
        while True:
            curr_emission = np.random.choice(len(possible_emissions), p=possible_emissions)
            curr_stress = poetrytools.stress(words[curr_emission])
            if len(curr_stress) == 1:
                prev_starting_stress = 1 - prev_starting_stress
                syllables_left -= 1
                break
            elif len(curr_stress) > syllables_left or int(curr_stress[-1]) == prev_starting_stress:
                continue
            else:
                prev_starting_stress = int(curr_stress[0])
                syllables_left -= len(curr_stress)
                break
        line.append(curr_emission)

    return line

def convert_line(sample, words):
    ret = ''
    i = 0
    for word in reversed(sample):
        curr_word = words[word]
        if i == 0 or (curr_word == 'i'):
            ret += curr_word.title() + ' '
        else:
            ret += curr_word + ' '
        i += 1
    return ret

def generate_pair(model, words, rhymes):
    while True:
        a_line = generate_line(model, words)
        seed = a_line[0]
        if len(np.where(rhymes[seed] == 1)[0]) > 0:
            b_line = generate_line(model, words, seed, rhymes)
            return a_line, b_line
        
def generate_rhyming_and_meter_sonnet():
    sonnet = ''
    a_lines = []
    b_lines = []
    
    for _ in range(4):
        a_line, b_line = generate_pair(reversed_quatrain_model, quatrain_words, quatrain_rhymes)
        a_lines.append(a_line)
        b_lines.append(b_line)
    
    for i in range(2):
        sonnet += convert_line(a_lines[2 * i], quatrain_words) + '\n'
        sonnet += convert_line(a_lines[2 * i + 1], quatrain_words) + '\n'
        sonnet += convert_line(b_lines[2 * i], quatrain_words) + '\n'
        sonnet += convert_line(b_lines[2 * i + 1], quatrain_words) + '\n'
    
    a_lines = []
    b_lines = []
    
    for _ in range(2):
        a_line, b_line = generate_pair(reversed_volta_model, volta_words, volta_rhymes)
        a_lines.append(a_line)
        b_lines.append(b_line)
    
    sonnet += convert_line(a_lines[0], volta_words) + '\n'
    sonnet += convert_line(a_lines[1], volta_words) + '\n'
    sonnet += convert_line(b_lines[0], volta_words) + '\n'
    sonnet += convert_line(b_lines[1], volta_words) + '\n'
    
    a_line, b_line = generate_pair(reversed_couplet_model, couplet_words, couplet_rhymes)
    sonnet += convert_line(a_line, couplet_words) + '\n'
    sonnet += convert_line(b_line, couplet_words) + '\n'
    
    return sonnet

def generate_10_rhyming_and_meter_sonnets():
    sonnets = ''
    for i in range(10):
        print('Generating Sonnet ' + str(i + 1))
        sonnets += str(i) + '\n' + generate_rhyming_and_meter_sonnet() + '\n'
    
    f = open("project2data/rhyming_and_meter_shakespeare.txt","w")
    f.write(sonnets)
    return sonnets