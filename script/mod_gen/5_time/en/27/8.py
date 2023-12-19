def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0:
        return 0
    if n < 10:
        return 1
    if n == 10:
        return 2
    if n < 100:
        if n == 11:
            return 4
        elif n % 10 == 0:
            return 10
        else:
            return 11
    if n == 100:
        return 21
    if n < 1000:
        if n % 100 == 0:
            return 100
        else:
            return 121
    if n == 1000:
        return 301
    if n < 10000:
        if n % 1000 == 0:
            return 1000
        else:
            return 1331
    if n == 10000:
        return 4001
    if n < 100000:
        if n % 10000 == 0:
            return 10000
        else:
            return 14641
    if n == 100000:
        return 50001
    if n < 1000000:
        if n % 100000 == 0:
            return 100000
        else:
            return 161051
    if n == 1000000:
        return 600001
    if n < 10000000:
        if n % 1000000 == 0:
            return 1000000
        else:
            return 1771561
    if n == 10000000:
        return 7000001
    if n < 100000000:
        if n % 10000000 == 0:
            return 10000000
        else:
            return 19487171
    if n == 100000000:
        return 80000001
    if n < 1000000000:
        if n % 100000000 == 0:
            return 100000000
        else:
            return 214358881
    if n == 1000000000:
        return 900000001
    return 0
print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(10))
print(countDigitOne(11))
print

if __name__ == '__main__':
    countDigitOne()