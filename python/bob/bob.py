import string


def response(hey_bob):
    hey_bob = hey_bob.replace('\t', '').strip()
    if not hey_bob:
        return "Fine. Be that way!"

    if hey_bob[-1] == '?':
        if any(char.upper() in string.ascii_uppercase for char in list(hey_bob)) and hey_bob.upper() == hey_bob:
            return "Calm down, I know what I'm doing!"
        else:
            return 'Sure.'

    if any(char.upper() in string.ascii_uppercase for char in list(hey_bob)) and hey_bob.upper() == hey_bob:
        return "Whoa, chill out!"
    else:
        return "Whatever."
