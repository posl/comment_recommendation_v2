def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0:
        return 0
    if n < 10:
        return 1
    base = 10
    while base <= n:
        base *= 10
    base //= 10
    first = n // base
    remain = n % base
    if first == 1:
        return countDigitOne(base - 1) + remain + 1 + countDigitOne(remain)
    else:
        return base + first * countDigitOne(base - 1) + countDigitOne(remain)
print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(10))
print(countDigitOne(100))
print(countDigitOne(1000))
print(countDigitOne(10000))
print(countDigitOne(100000))
print(countDigitOne(1000000))
print(countDigitOne(10000000))
print(countDigitOne(100000000))
print(countDigitOne(1000000000))
