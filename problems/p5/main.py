''''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

from problems import get_prime_factors


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
