import math
import time

from problems import is_prime


def main():
    stop = 10001
    # primes = []
    # primes.append(iterator)
    start = time.time()
    iterator = 1
    prime_count = 0
    while True:
        iterator += 1
        if is_prime(iterator):
            prime_count+= 1
        if prime_count >= stop:
            break
    print(f"prime #{stop} is {iterator}")
    print(f"took {time.time() - start} amount of time")

if __name__ == '__main__':
    main()
