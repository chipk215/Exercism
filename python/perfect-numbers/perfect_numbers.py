
def get_aliquot(number):
    factors = []
    for i in range(1, (number // 2) + 1):
        if number % i == 0:
            factors.append(i)

    return sum(factors)


def classify(number):
    if number < 1:
        raise ValueError('Numbers must be greater than 0')

    aliquot = get_aliquot(number)
    if aliquot == number:
        return 'perfect'
    if aliquot < number:
        return 'deficient'
    return 'abundant'
