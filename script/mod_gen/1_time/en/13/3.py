def numSteps(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n += 1
        count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    a = numSteps(n)
    print(a)