def nthUglyNumber(n):
    ugly = [1]
    i2, i3, i5 = 0, 0, 0
    while len(ugly) < n:
        while ugly[i2] * 2 <= ugly[-1]:
            i2 += 1
        while ugly[i3] * 3 <= ugly[-1]:
            i3 += 1
        while ugly[i5] * 5 <= ugly[-1]:
            i5 += 1
        ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
    return ugly[-1]
print(nthUglyNumber(10))
print(nthUglyNumber(1))
print(nthUglyNumber(1690))
print(nthUglyNumber(2))
print(nthUglyNumber(3))
print(nthUglyNumber(4))
print(nthUglyNumber(5))
print(nthUglyNumber(6))
print(nthUglyNumber(7))
print(nthUglyNumber(8))
print(nthUglyNumber(9))
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
print(nthUglyNumber(39
