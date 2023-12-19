def main():
    n = int(input("Enter n: "))
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        elif n % 2 != 0:
            if n == 3:
                n = n - 1
            elif (n + 1) % 4 == 0:
                n = n + 1
            else:
                n = n - 1
        count += 1
    print(count)

if __name__ == '__main__':
    main()