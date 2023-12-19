def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    ugly = [1]
    i2, i3, i5 = 0, 0, 0
    while n > 1:
        u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
        umin = min((u2, u3, u5))
        if umin == u2:
            i2 += 1
        if umin == u3:
            i3 += 1
        if umin == u5:
            i5 += 1
        ugly.append(umin)
        n -= 1
    return ugly[-1]
print(nthUglyNumber(10))
print(nthUglyNumber(1))
print(nthUglyNumber(11))
print(nthUglyNumber(12))
print(nthUglyNumber(13))
print(nthUglyNumber(14))
print(nthUglyNumber(15))
print(nthUglyNumber(16))
print(nthUglyNumber(17))
print(nthUglyNumber(18))
print(nthUglyNumber(19))
print(nthUglyNumber(20))
print(nthUglyNumber(21))
print(nthUglyNumber(22))
print(nthUglyNumber(23))
print(nthUglyNumber(24))
print(nthUglyNumber(25))
print(nthUglyNumber(26))
print(nthUglyNumber(27))
print(nthUglyNumber(28))
print(nthUglyNumber(29))
print(nthUglyNumber(30))
print(nthUglyNumber(31))
print(nthUglyNumber(32))
print(nthUglyNumber(33))
print(nthUglyNumber(34))
print(nthUglyNumber(35))
print(nthUglyNumber(36))
print(nthUglyNumber(37))
print(nthUglyNumber(38))
print(nthUglyNumber(39))
print(nthUglyNumber(40))
print(nthUglyNumber(41))
print(nthUglyNumber(42))
print(nthUglyNumber(43))
print(nthUglyNumber(44))
print(nthUglyNumber(45))
print(nth

if __name__ == '__main__':
    nthUglyNumber()