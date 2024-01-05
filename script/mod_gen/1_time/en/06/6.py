def nthUglyNumber(n):
    ugly = [0] * n
    ugly[0] = 1
    i2 = i3 = i5 = 0
    for i in range(1, n):
        ugly[i] = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
        if ugly[i] == ugly[i2] * 2:
            i2 += 1
        if ugly[i] == ugly[i3] * 3:
            i3 += 1
        if ugly[i] == ugly[i5] * 5:
            i5 += 1
    return ugly[-1]
print(nthUglyNumber(10))
print(nthUglyNumber(1))
print(nthUglyNumber(11))
print("The values above should be 12, 1, and 15.")

if __name__ == '__main__':
    n = int(input())
    a = nthUglyNumber(n)
    print(a)