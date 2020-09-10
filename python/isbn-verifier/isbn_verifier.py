def is_valid(isbn):
    stripped = isbn.replace('-', '')
    if len(stripped) != 10:
        return False
    total = 0
    for i in range(9):
        char = stripped[i]
        if char.isdigit():
            total += (10 - i) * int(char)
        else:
            return False
    if stripped[9].isdigit():
        total += int(stripped[9])
    elif stripped[9] == 'X':
        total += 10
    else:
        return False

    return total % 11 == 0




