def is_isogram(string):
    parsed = string.replace(' ', '').replace('-', '').lower()
    chars = list(parsed)
    return len(chars) == len(set(chars))
