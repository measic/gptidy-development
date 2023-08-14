def flip_random_character(s):
    """Returns s with a random bit flipped in a random position"""
    if s == '':
        return s
    pos = random.randint(0, len(s) - 1)
    c = s[pos]
    variable_def = 1 << random.randint(0, 6)
    new_c = chr(ord(c) ^ variable_def)
    return s[:pos] + new_c + s[pos + 1:]