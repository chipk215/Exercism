
def get_factors(number, min_factor, max_factor):
    factors = []
    for i in range(min_factor, max_factor + 1):
        if number % i == 0:
            pair_factor = number // i
            if min_factor <= pair_factor <= max_factor:
                factors.append(i)
    return factors


def is_palidrome_number(number):
    num_str = str(number)
    if num_str == num_str[::-1]:
        return True
    return False


def largest(min_factor, max_factor):
    """ The frist palindrome is not always the largest .. bah"""
    if max_factor < min_factor:
        raise ValueError('min_factor must be less than max_factor')
    palindrome = None
    factor_results = []
    max_product = 0
    for i in range(max_factor, min_factor-1, -1):
        for j in range(i, min_factor - 1, -1):
            product = i * j
            if is_palidrome_number(product):
                if product > max_product:
                    palindrome = product
                    max_product = product
                    factor_results = []
                    factors = get_factors(product, min_factor, max_factor)
                    for factor in factors:
                        f2 = product // factor
                        if factor < f2:
                            pair = [factor, f2]
                        else:
                            pair = [f2, factor]
                        if pair not in factor_results:
                            factor_results.append(pair)

    return palindrome, factor_results


def smallest(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError('min_factor must be less than max_factor')

    palindrome = None
    factor_results = []
    min_product = max_factor * max_factor
    for i in range(min_factor, max_factor+1):
        for j in range(i, max_factor+1):
            product = i * j
            if is_palidrome_number(product):
                if product < min_product:
                    palindrome = product
                    min_product = product
                    factor_results = []
                    factors = get_factors(product, min_factor, max_factor)
                    for factor in factors:
                        f2 = product // factor
                        if factor < f2:
                            pair = [factor, f2]
                        else:
                            pair = [f2, factor]
                        if pair not in factor_results:
                            factor_results.append(pair)

    return palindrome, factor_results
