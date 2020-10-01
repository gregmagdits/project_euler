# complexity here?
# worst case is the number is prime, so it would be number/2
# best case is the number is even so it would be log number
def get_factors(number):
    i = 2
    factors = []
    while i < number/2:
        if number % i == 0:
            factors.append(i)
            number = number / i
            i = 2
        else:
            i+=1
    factors.append(number)
    return factors


def main():
    factors = get_factors(600851475143 )
    print(f"factors is {factors}")


if __name__ == '__main__':
    main()
