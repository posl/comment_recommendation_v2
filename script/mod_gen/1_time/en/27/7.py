def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 1:
        return 0
    elif n < 10:
        return 1
    elif n < 20:
        return 2
    elif n < 100:
        return 20 + countDigitOne(n % 10) + countDigitOne(n // 10)
    elif n < 200:
        return 20 + 10 * countDigitOne(n % 100) + countDigitOne(n // 100)
    elif n < 1000:
        return 300 + countDigitOne(n % 100) + countDigitOne(n // 100)
    elif n < 2000:
        return 300 + 100 * countDigitOne(n % 1000) + countDigitOne(n // 1000)
    elif n < 10000:
        return 4000 + countDigitOne(n % 1000) + countDigitOne(n // 1000)
    elif n < 20000:
        return 4000 + 1000 * countDigitOne(n % 10000) + countDigitOne(n // 10000)
    elif n < 100000:
        return 50000 + countDigitOne(n % 10000) + countDigitOne(n // 10000)
    elif n < 200000:
        return 50000 + 10000 * countDigitOne(n % 100000) + countDigitOne(n // 100000)
    elif n < 1000000:
        return 600000 + countDigitOne(n % 100000) + countDigitOne(n // 100000)
    elif n < 2000000:
        return 600000 + 100000 * countDigitOne(n % 1000000) + countDigitOne(n // 1000000)
    elif n < 10000000:
        return 7000000 + countDigitOne(n % 1000000) + countDigitOne(n // 1000000)
    elif n < 20000000:
        return 7000000 + 1000000 * countDigitOne(n % 10000000) + countDigitOne(n // 10000000)
    elif n < 100000000:
        return 80000000 + countDigitOne(n % 100

if __name__ == '__main__':
    n = int(input())
    a = countDigitOne(n)
    print(a)