def square(number):
    if number < 1 or number > 64:
        raise ValueError("Number of square must be between 1 and 64")

    return 2 ** (number - 1)


def total():
    """
    Sum of geometric series https://www.varsitytutors.com/hotmath/hotmath_help/topics/geometric-series.html
    :return:
    """
    return int((1 - (2 ** 64))) // (1-2)
