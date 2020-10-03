''''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''
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


def get_minimum_common_multiple(start, stop):
    all_prime_factors = []
    for i in range(start, stop + 1):
        prime_factors = get_prime_factors(i)
        print(f"debugging")
        for item in all_prime_factors:
            if item in prime_factors:
                prime_factors.remove(item)
        all_prime_factors.extend(prime_factors)
    print(f"prime factors are {all_prime_factors}")
    answer = 1
    for factor in all_prime_factors:
        answer *= factor
    return answer


def main():
    start = 1
    stop = 20
    product = get_minimum_common_multiple(start, stop)
    print(f"product = {product}")


if __name__ == '__main__':
    main()
