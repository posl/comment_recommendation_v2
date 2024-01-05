def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 1:
        return 0
    if n < 10:
        return 1
    if n < 20:
        return 2
    if n < 100:
        return 20 + countDigitOne(n % 10) + countDigitOne(n / 10 - 1)
    if n < 200:
        return 20 + countDigitOne(n % 100) + countDigitOne(n / 100)
    if n < 1000:
        return 300 + countDigitOne(n % 100) + countDigitOne(n / 100 - 1)
    if n < 2000:
        return 300 + countDigitOne(n % 1000) + countDigitOne(n / 1000)
    if n < 10000:
        return 4000 + countDigitOne(n % 1000) + countDigitOne(n / 1000 - 1)
    if n < 20000:
        return 4000 + countDigitOne(n % 10000) + countDigitOne(n / 10000)
    if n < 100000:
        return 50000 + countDigitOne(n % 10000) + countDigitOne(n / 10000 - 1)
    if n < 200000:
        return 50000 + countDigitOne(n % 100000) + countDigitOne(n / 100000)
    if n < 1000000:
        return 600000 + countDigitOne(n % 100000) + countDigitOne(n / 100000 - 1)
    if n < 2000000:
        return 600000 + countDigitOne(n % 1000000) + countDigitOne(n / 1000000)
    if n < 10000000:
        return 7000000 + countDigitOne(n % 1000000) + countDigitOne(n / 1000000 - 1)
    if n < 20000000:
        return 7000000 + countDigitOne(n % 10000000) + countDigitOne(n / 10000000)
    if n < 100000000:
        return 80000000 + countDigitOne(n % 10000000) + count

if __name__ == '__main__':
    n = int(input())
    a = countDigitOne(n)
    print(a)