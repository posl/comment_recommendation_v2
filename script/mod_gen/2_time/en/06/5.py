def nthUglyNumber(n):
    if n == 1:
        return 1
    ugly = [1]
    i2 = 0
    i3 = 0
    i5 = 0
    while n > 1:
        u2 = ugly[i2] * 2
        u3 = ugly[i3] * 3
        u5 = ugly[i5] * 5
        umin = min(u2, u3, u5)
        if umin == u2:
            i2 += 1
        if umin == u3:
            i3 += 1
        if umin == u5:
            i5 += 1
        ugly.append(umin)
        n -= 1
    return ugly[-1]

if __name__ == '__main__':
    nthUglyNumber()