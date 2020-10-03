'''

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''
def get_domain(digits):
    return range(0, 10 ** (digits*2))


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def test_possible_answer(digits, possible_answer):
    max_n = int('9' * digits)
    min_n = int( '1' + ('0' * (digits-1)))
    for i in range(max_n, min_n, -1):
        factor = possible_answer / i
        if int(factor) == factor and min_n <= factor <= max_n:
            return True
    return False


def largest_palindrome_less_than(largest_n):
    pass


def largest_product(digits):
    return int('9' * digits) ** 2


def main():
    digits = 3
    domain = get_domain(3)
    # complexity here is 2n, for 10^6, this should be a 2-5 seconds
    palindromes = [n for n in domain if is_palindrome(n)]
    palindromes.reverse()
    for p in palindromes:
        if test_possible_answer(digits, p):
            print(f"answer is {p}")
            exit()

#    largest_n = largest_product(3)
#    while True:
#        p = largest_palindrome_less_than(largest_n)
#        if test_possible_answer(digits, p):
#            print(f"answer is {p}")
#            exit(0)
#        else:
#            largest_n = p

    '''
        find the largest palindromes less than possible and for each, decompose into product of 2 numbers check to see if it is a product of 2, 3 digit numbers?
        or find largest 
    '''


if __name__ == '__main__':
    main()
