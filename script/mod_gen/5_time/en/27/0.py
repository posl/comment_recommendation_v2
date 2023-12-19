def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 1:
        return 0
    count = 0
    i = 1
    while i <= n:
        divider = i * 10
        count += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
        i *= 10
    return count
print(countDigitOne(13)) # 6
print(countDigitOne(0)) # 0
print(countDigitOne(1)) # 1
print(countDigitOne(10)) # 2
print(countDigitOne(11)) # 4
print(countDigitOne(12)) # 5
print(countDigitOne(20)) # 12
print(countDigitOne(21)) # 13
print(countDigitOne(22)) # 14
print(countDigitOne(23)) # 15
print(countDigitOne(24)) # 16
print(countDigitOne(25)) # 17
print(countDigitOne(26)) # 18
print(countDigitOne(27)) # 19
print(countDigitOne(28)) # 20
print(countDigitOne(29)) # 21
print(countDigitOne(30)) # 22
print(countDigitOne(31)) # 24
print(countDigitOne(32)) # 25
print(countDigitOne(33)) # 26
print(countDigitOne(34)) # 27
print(countDigitOne(35)) # 28
print(countDigitOne(36)) # 29
print(countDigitOne(37)) # 30
print(countDigitOne(38)) # 31
print(countDigitOne(39)) # 32
print(countDigitOne(40)) # 33
print(countDigitOne(41)) # 35
print(countDigitOne(42)) # 36
print(countDigitOne(43)) # 37
print(countDigitOne(44)) # 38
print(countDigitOne(45)) # 39
print(countDigitOne(46)) # 40
print(countDigitOne(47)) # 41
print(countDigitOne(48)) # 42
print(countDigitOne(49)) # 43
print(countDigitOne(50))
