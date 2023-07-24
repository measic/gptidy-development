def to_appropriate_column_name(s):
    s = s.lower().replace(' ', '_')
    s = ''.join([ch for ch in s if ch.isalnum() or ch == '_'])
    return s