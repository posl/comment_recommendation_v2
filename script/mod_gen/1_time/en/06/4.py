def nthUglyNumber(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    t2 = t3 = t5 = 0
    res = [0] * n
    res[0] = 1
    for i in range(1, n):
        res[i] = min(res[t2] * 2, res[t3] * 3, res[t5] * 5)
        if res[i] == res[t2] * 2:
            t2 += 1
        if res[i] == res[t3] * 3:
            t3 += 1
        if res[i] == res[t5] * 5:
            t5 += 1
    return res[-1]
print(nthUglyNumber(10))
print(nthUglyNumber(1))
print(nthUglyNumber(1690))
print(nthUglyNumber(0))
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
print(nthUgly

if __name__ == '__main__':
    nthUglyNumber()