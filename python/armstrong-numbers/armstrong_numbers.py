def is_armstrong_number(number):
    str_number = str(number)
    num_digits = len(str_number)
    total = 0
    for digit in str_number:
        total += int(digit) ** num_digits

    return total == number

