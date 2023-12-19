def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0:
        return 0
    if n < 10:
        return 1
    if n >= 10 and n < 20:
        return n - 9
    if n >= 20 and n < 100:
        return 11 + countDigitOne(n % 10) + countDigitOne(n / 10)
    if n >= 100 and n < 1000:
        return 11 * (n / 100) + countDigitOne(n % 100) + countDigitOne(n / 100) * (n % 100 + 1)
    if n >= 1000 and n < 10000:
        return 11 * (n / 1000) + countDigitOne(n % 1000) + countDigitOne(n / 1000) * (n % 1000 + 1)
    if n >= 10000 and n < 100000:
        return 11 * (n / 10000) + countDigitOne(n % 10000) + countDigitOne(n / 10000) * (n % 10000 + 1)
    if n >= 100000 and n < 1000000:
        return 11 * (n / 100000) + countDigitOne(n % 100000) + countDigitOne(n / 100000) * (n % 100000 + 1)
    if n >= 1000000 and n < 10000000:
        return 11 * (n / 1000000) + countDigitOne(n % 1000000) + countDigitOne(n / 1000000) * (n % 1000000 + 1)
    if n >= 10000000 and n < 100000000:
        return 11 * (n / 10000000) + countDigitOne(n % 10000000) + countDigitOne(n / 10000000) * (n % 10000000 + 1)
    if n >= 100000000 and n < 1000000000:
        return 11 * (n / 100000000) + countDigitOne(n % 100000000) + countDigitOne(n / 100000000

if __name__ == '__main__':
    countDigitOne()