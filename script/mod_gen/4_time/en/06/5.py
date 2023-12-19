def nthUglyNumber(n):
    ugly_numbers = [1]
    i2, i3, i5 = 0, 0, 0
    while len(ugly_numbers) < n:
        next2 = ugly_numbers[i2] * 2
        next3 = ugly_numbers[i3] * 3
        next5 = ugly_numbers[i5] * 5
        next_ugly = min(next2, next3, next5)
        ugly_numbers.append(next_ugly)
        if next_ugly == next2:
            i2 += 1
        if next_ugly == next3:
            i3 += 1
        if next_ugly == next5:
            i5 += 1
    return ugly_numbers[-1]
print(nthUglyNumber(10))
print(nthUglyNumber(1))
print(nthUglyNumber(10))
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
print(n

if __name__ == '__main__':
    nthUglyNumber()