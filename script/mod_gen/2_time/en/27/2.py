def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0:
        return 0
    num = n
    base = 1
    total = 0
    while num > 0:
        last = num % 10
        num = num // 10
        total += num * base
        if last == 1:
            total += n % base + 1
        elif last > 1:
            total += base
        base *= 10
    return total
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
print(countDigitOne(10000000000))
print(countDigitOne(100000000000))
print(countDigitOne(1000000000000))
print(countDigitOne(10000000000000))
print(countDigitOne(100000000000000))
print(countDigitOne(1000000000000000))
print(countDigitOne(10000000000000000))
print(countDigitOne(100000000000000000))
print(countDigitOne(1000000000000000000))
print(countDigitOne(10000000000000000000))
print(countDigitOne(100000000000000000000))
print(countDigitOne(1000000000000000000000))
print(countDigitOne(10000000000000000000000))
print(countDigitOne(100000000000000000000000))
print(countDigitOne(1000000000000000000000000))
print(countDigitOne(10000000000000000000000000))
print(countDigitOne(100000000000000000000000000))
print(countDigitOne(1000000000000000000000000000))
print(countDigitOne(10000000000000000000000000000))
print(countDigitOne(100000000000000000000000000000))
print(countDigitOne(1000000000000000000000000000000))
print(countDigitOne(100000000000000000
