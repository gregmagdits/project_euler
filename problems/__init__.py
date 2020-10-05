import math


def get_prime_factors(number_to_decompose):
    factors = []
    test_numbers = list(range(2, math.floor(number_to_decompose / 2) + 1))
    for index in range(0, len(test_numbers)):
        n = test_numbers[index]
        if number_to_decompose % n == 0 and n not in factors:
            other_factor = int(number_to_decompose / n)
            factors.extend(get_prime_factors(n))
            factors.extend(get_prime_factors(other_factor))
            break

    if not factors:
        # n itself must be prime
        factors.append(number_to_decompose)
    return factors


def is_even(num):
    return num & 1 == 0


def is_prime(maybe_prime):
    if maybe_prime in [1, 2]:
        return True
    if is_even(maybe_prime):
        return False
    for n in range(3, math.floor(maybe_prime / 2) + 1):
        if maybe_prime % n == 0:
            return False
    return True
