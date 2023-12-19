def nthUglyNumber(n):
    ugly = [1]
    i2 = i3 = i5 = 0
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
print(nthUglyNumber(1691))
print(nthUglyNumber(1692))
print(nthUglyNumber(1693))
print(nthUglyNumber(1694))
print(nthUglyNumber(1695))
print(nthUglyNumber(1696))
print(nthUglyNumber(1697))
print(nthUglyNumber(1698))
print(nthUglyNumber(1699))
print(nthUglyNumber(1700))
print(nthUglyNumber(1701))
print(nthUglyNumber(1702))
print(nthUglyNumber(1703))
print(nthUglyNumber(1704))
print(nthUglyNumber(1705))
print(nthUglyNumber(1706))
print(nthUglyNumber(1707))
print(nthUglyNumber(1708))
print(nthUglyNumber(1709))
print(nthUglyNumber(1710))
print(nthUglyNumber(1711))
print(nthUglyNumber(1712))
print(nthUglyNumber(1713))
print(nthUglyNumber(1714))
print(nthUglyNumber(1715))
print(nthUglyNumber(1716))
print(nthUglyNumber(1717))
print(nthUglyNumber(1718))
print(nthUglyNumber(1719))
print(nthUglyNumber(1720))
print(nthUglyNumber(1721))
print(nthUglyNumber(1722))
print(nthUglyNumber(1723))
print(nthUglyNumber(172
