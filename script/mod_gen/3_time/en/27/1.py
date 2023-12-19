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
        return 20 + 10*(n-19) + countDigitOne(n-10*(n-19))
    if n < 200:
        return 20 + 10*(n-99) + countDigitOne(n-10*(n-99))
    if n < 1000:
        return 300 + 100*(n-199) + countDigitOne(n-100*(n-199))
    if n < 2000:
        return 300 + 100*(n-999) + countDigitOne(n-100*(n-999))
    if n < 10000:
        return 4000 + 1000*(n-1999) + countDigitOne(n-1000*(n-1999))
    if n < 20000:
        return 4000 + 1000*(n-9999) + countDigitOne(n-1000*(n-9999))
    if n < 100000:
        return 50000 + 10000*(n-19999) + countDigitOne(n-10000*(n-19999))
    if n < 200000:
        return 50000 + 10000*(n-99999) + countDigitOne(n-10000*(n-99999))
    if n < 1000000:
        return 600000 + 100000*(n-199999) + countDigitOne(n-100000*(n-199999))
    if n < 2000000:
        return 600000 + 100000*(n-999999) + countDigitOne(n-100000*(n-999999))
    if n < 10000000:
        return 7000000 + 1000000*(n-1999999) + countDigitOne(n-1000000*(n-1999999))
    if n < 20000000:
        return 7000000 + 1000000*(n-9999999) + countDigitOne(n-1000000*(n-9999999))
    if n < 100

if __name__ == '__main__':
    countDigitOne()