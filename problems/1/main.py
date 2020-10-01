
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

# This works but is kind of slow
#sum = 0
#for i in range(0,1000):
#    if i % 3 == 0 or i % 5 == 0:
#        sum += i


def multiples(base, limit=1000):
    multiplier = 1
    multiples = set()
    while True:
        multiple = base * multiplier
        if multiple < limit:
            multiples.add(multiple)
            multiplier += 1
        else:
            break
    return multiples

def main():
    all_multiples = set()
    all_multiples.update(multiples(3))
    all_multiples.update(multiples(5))
    print(f"sum of multiples is {sum(all_multiples)}")

if __name__ == '__main__':
    main()