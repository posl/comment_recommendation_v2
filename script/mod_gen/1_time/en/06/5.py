def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    if n==1:
        return 1
    ugly=[1]
    i2=i3=i5=0
    for i in range(1,n):
        ugly.append(min(ugly[i2]*2,ugly[i3]*3,ugly[i5]*5))
        if ugly[i]==ugly[i2]*2:
            i2+=1
        if ugly[i]==ugly[i3]*3:
            i3+=1
        if ugly[i]==ugly[i5]*5:
            i5+=1
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
