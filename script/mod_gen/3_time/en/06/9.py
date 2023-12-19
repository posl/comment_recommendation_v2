def nthUglyNumber(n):
    ugly = [1]
    i2 = i3 = i5 = 0
    while len(ugly) < n:
        while ugly[i2] * 2 <= ugly[-1]: i2 += 1
        while ugly[i3] * 3 <= ugly[-1]: i3 += 1
        while ugly[i5] * 5 <= ugly[-1]: i5 += 1
        ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
    return ugly[-1]
print(nthUglyNumber(10)) #12
print(nthUglyNumber(1)) #1
print(nthUglyNumber(1690)) #2123366400
print(nthUglyNumber(1600)) #1399680000
print(nthUglyNumber(100)) #1536
print(nthUglyNumber(50)) #243
print(nthUglyNumber(20)) #36
print(nthUglyNumber(1690)) #2123366400
print(nthUglyNumber(1690)) #2123366400
print(nthUglyNumber
