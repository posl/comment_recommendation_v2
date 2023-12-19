def nthUglyNumber(n):
    ugly = [0] * n
    ugly[0] = 1
    i2 = i3 = i5 = 0
    for l in range(1, n):
        ugly[l] = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
        if ugly[l] == ugly[i2] * 2:
            i2 += 1
        if ugly[l] == ugly[i3] * 3:
            i3 += 1
        if ugly[l] == ugly[i5] * 5:
            i5 += 1
    return ugly[-1]
print(nthUglyNumber(10))
print(nthUglyNumber(1))
