def integerBreak(n):
    if n == 2:
        return 1
    if n == 3:
        return 2
    
    product = 1
    while n > 4:
        product *= 3
        n -= 3
    product *= n
    return product
print(integerBreak(10))
print(integerBreak(2))
print(integerBreak(3))
print(integerBreak(4))
print(integerBreak(5))
print(integerBreak(6))
print(integerBreak(7))
print(integerBreak(8))
print(integerBreak(9))
print(integerBreak(10))
print(integerBreak(11))
print(integerBreak(12))
print(integerBreak(13))
print(integerBreak(14))
print(integerBreak(15))
print(integerBreak(16))
print(integerBreak(17))
print(integerBreak(18))
print(integerBreak(19))
print(integerBreak(20))
print(integerBreak(21))
print(integerBreak(22))
print(integerBreak(23))
print(integerBreak(24))
print(integerBreak(25))
print(integerBreak(26))
print(integerBreak(27))
print(integerBreak(28))
print(integerBreak(29))
print(integerBreak(30))
print(integerBreak(31))
print(integerBreak(32))
print(integerBreak(33))
print(integerBreak(34))
print(integerBreak(35))
print(integerBreak(36))
print(integerBreak(37))
print(integerBreak(38))
print(integerBreak(39))
print(integerBreak(40))
print(integerBreak(41))
print(integerBreak(42))
print(integerBreak(43))
print(integerBreak(44))
print(integerBreak(45))
print(integerBreak(46))
print(integerBreak(47))
print(integerBreak(48))
print(integerBreak(49))
print(integerBreak(50))
print(integerBreak(51))
print(integerBreak(52))
print(integerBreak(53))
print(integerBreak(54))
print(integerBreak(55))
print(integerBreak(56))
print(integerBreak(57))
print(integerBreak(58))