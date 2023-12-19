def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    ugly = [1]
    i2 = 0
    i3 = 0
    i5 = 0
    for i in range(1, n):
        ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        if ugly[i] == ugly[i2] * 2:
            i2 += 1
        if ugly[i] == ugly[i3] * 3:
            i3 += 1
        if ugly[i] == ugly[i5] * 5:
            i5 += 1
    return ugly[-1]

if __name__ == '__main__':
    nthUglyNumber()