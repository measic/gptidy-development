def function_def(s):
    s = s.lower().replace(' ', '_')
    s = ''.join([ch for ch in s if ch.isalnum() or ch == '_'])
    return s