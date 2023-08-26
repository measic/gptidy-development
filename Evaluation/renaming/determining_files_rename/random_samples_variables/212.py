def flip_random_character(s):
    """Returns s with a random bit flipped in a random position"""
    if s == '':
        return s
    pos = random.randint(0, len(s) - 1)
    c = s[pos]
    bit = 1 << random.randint(0, 6)
    variable_def = chr(ord(c) ^ bit)
    return s[:pos] + variable_def + s[pos + 1:]