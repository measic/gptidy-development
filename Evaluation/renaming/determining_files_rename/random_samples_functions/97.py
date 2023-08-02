def function_def(s):
    """Returns s with a random character deleted"""
    if s == '':
        return s
    pos = random.randint(0, len(s) - 1)
    return s[:pos] + s[pos + 1:]