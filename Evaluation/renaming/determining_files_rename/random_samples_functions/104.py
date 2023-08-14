def hypothesis_inlinecounter(text):
    hyp = np.concatenate([np.linspace(1, -1, len(x) + 1) for x in text.split('\n')])[:-1]
    return hyp

def hypothesis_capswords(text):
    hyp = np.concatenate([np.full(len(x) + 1, 1) if re.sub('[^a-zA-Z]+', '', x).isupper() else np.full(len(x) + 1, -1) for x in text.split('\n')])[:-1]
    return hyp

def hypothesis_pos(text, pos_tag):
    hyp = text.replace('1', '0')
    for word, tag in pynlpir.segment(text):
        if tag == pos_tag:
            hyp = hyp.replace(word, '1' * len(word), 1)
        else:
            hyp = hyp.replace(word, '0' * len(word), 1)
    hyp = [1 if x == '1' else -1 for x in re.sub('[^1]', '0', hyp)]
    return hyp

def hypothesis_verbs(text):
    return hypothesis_pos(text, 'verb')

def function_def(text):
    return hypothesis_pos(text, 'noun')