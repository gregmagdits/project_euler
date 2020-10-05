

def main():
    start =1
    stop = 100
    sum = 0
    for i in range(start, stop + 1):
        sum += i
    sqaured_sum = sum ** 2

    sum = 0
    for i in range(start, stop + 1):
        sum += i**2

    sum_of_sqares = sum

    print (f"answer is {sqaured_sum - sum_of_sqares}")


if __name__ == '__main__':
    main()
