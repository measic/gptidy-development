def hypothesis_inlinecounter(text):
    hyp = np.concatenate([np.linspace(1, -1, len(x) + 1) for x in text.split('\n')])[:-1]
    return hyp

def hypothesis_inside_one(text, single):
    hyp = re.sub('\\{}.*?\\{}'.format(single, single), lambda m: single + '#' * (len(m.group()) - 2) + single, text)
    return np.array([1 if x == '#' else -1 for x in hyp])

def hypothesis_inside_two(text, left, right):
    hyp = np.full(len(text), -1)
    inside = False
    for i in range(len(text) - 1):
        if text[i] == left:
            inside = True
        elif text[i] == right:
            inside = False
        if inside:
            hyp[i + 1] = 1
    return hyp
hypothesis_inside_quotation = lambda x: hypothesis_inside_one(x, '"')
hypothesis_inside_parantheses = lambda x: hypothesis_inside_two(x, '(', ')')

def function_def(text):
    hyp = np.full(len(text), -1)
    in_brac_comment = False
    in_line_comment = False
    for i in range(len(text)):
        if text[i:i + 2] == '//':
            in_line_comment = True
        elif text[i] == '\n':
            in_line_comment = False
        elif text[i:i + 2] == '/*':
            in_brac_comment = True
        elif text[i:i + 2] == '*/':
            in_brac_comment = False
        if in_brac_comment:
            hyp[i:i + 3] = 1
        if in_line_comment:
            hyp[i:i + 1] = 1
    return hyp

def hypothesis_indentation(text, level):
    hyp = np.full(len(text), -1)
    cur_level = 0
    for i, char in enumerate(text):
        if char == '\n':
            cur_level = 0
        elif char == '\t':
            cur_level += 1
        if cur_level >= level:
            hyp[i] = 1
    return hyp