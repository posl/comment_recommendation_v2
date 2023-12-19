def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0:
        return 0
    q, x, ans = n, 1, 0
    while q > 0:
        digit = q % 10
        q //= 10
        ans += q * x
        if digit == 1:
            ans += n % x + 1
        elif digit > 1:
            ans += x
        x *= 10
    return ans
print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(10))
print(countDigitOne(20))
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
