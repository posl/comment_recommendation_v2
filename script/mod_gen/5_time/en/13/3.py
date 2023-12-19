def reduceTo1(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n + 1
        count = count + 1
    return count

if __name__ == '__main__':
    reduceTo1()