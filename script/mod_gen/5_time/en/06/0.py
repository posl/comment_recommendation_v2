def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    uglies = [1]
    i2 = i3 = i5 = 0
    while len(uglies) < n:
        while uglies[i2] * 2 <= uglies[-1]:
            i2 += 1
        while uglies[i3] * 3 <= uglies[-1]:
            i3 += 1
        while uglies[i5] * 5 <= uglies[-1]:
            i5 += 1
        uglies.append(min(uglies[i2] * 2, uglies[i3] * 3, uglies[i5] * 5))
    return uglies[-1]

if __name__ == '__main__':
    nthUglyNumber()