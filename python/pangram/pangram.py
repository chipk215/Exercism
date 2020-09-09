def is_pangram(sentence):
    def letter_only(c):
        ord_char = ord(c)
        if ord('a') <= ord_char <= ord('z'):
            return c
        return None
    sentence = sentence.lower()
    if len(sentence) == 0 or sentence is None:
        return False
    stripped_sentence = list(filter(None, map(letter_only, sentence)))
    characters = set(stripped_sentence)

    return len(characters) == 26
