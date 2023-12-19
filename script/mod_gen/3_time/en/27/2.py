def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    # if n < 1, return 0
    if n < 1:
        return 0
    # if n < 10, return 1
    if n < 10:
        return 1
    # if n < 100, return 20
    if n < 100:
        if n < 20:
            return 1 + n - 10 + 1
        else:
            return 20
    # if n < 1000, return 300
    if n < 1000:
        if n < 200:
            return 1 + countDigitOne(n-100) + 100
        else:
            return 300
    # if n < 10000, return 4000
    if n < 10000:
        if n < 2000:
            return 1 + countDigitOne(n-1000) + 1000
        else:
            return 4000
    # if n < 100000, return 50000
    if n < 100000:
        if n < 20000:
            return 1 + countDigitOne(n-10000) + 10000
        else:
            return 50000
    # if n < 1000000, return 600000
    if n < 1000000:
        if n < 200000:
            return 1 + countDigitOne(n-100000) + 100000
        else:
            return 600000
    # if n < 10000000, return 7000000
    if n < 10000000:
        if n < 2000000:
            return 1 + countDigitOne(n-1000000) + 1000000
        else:
            return 7000000
    # if n < 100000000, return 80000000
    if n < 100000000:
        if n < 20000000:
            return 1 + countDigitOne(n-10000000) + 10000000
        else:
            return 80000000
    # if n < 1000000000, return 900000000
    if n < 1000000000:
        if n

if __name__ == '__main__':
    countDigitOne()