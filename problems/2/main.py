

def is_even(num):
    return num & 1 == 0

def generate_fib(limit):
    sum =0

    fib_seq = [1,2]
    while sum < limit:
        sum = fib_seq[-1] + fib_seq[-2]
        if sum > limit:
            break
        else:
            fib_seq.append(sum)
    return fib_seq

def main():
    fib = generate_fib(limit=4*(10**6))
    answer = sum(f for f in fib if is_even(f))
    print(f"answer is {answer}")

if __name__ == '__main__':
    main()