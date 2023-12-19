def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    res = []
    for i in range(n+1):
        count = 0
        while i > 0:
            count += i & 1
            i >>= 1
        res.append(count)
    return res
print(countBits(2))
print(countBits(5))
print(countBits(10))
print(countBits(100))
print(countBits(1000))
print(countBits(10000))
print(countBits(100000))
print(countBits(1000000))
print(countBits(10000000))
print(countBits(100000000))
print(countBits(1000000000))
print(countBits(10000000000))
print(countBits(100000000000))
print(countBits(1000000000000))
print(countBits(10000000000000))
print(countBits(100000000000000))
print(countBits(1000000000000000))
print(countBits(10000000000000000))
print(countBits(100000000000000000))
print(countBits(1000000000000000000))
print(countBits(10000000000000000000))
print(countBits(100000000000000000000))
print(countBits(1000000000000000000000))
print(countBits(10000000000000000000000))
print(countBits(100000000000000000000000))
print(countBits(1000000000000000000000000))
print(countBits(10000000000000000000000000))
print(countBits(100000000000000000000000000))
print(countBits(1000000000000000000000000000))
print(countBits(10000000000000000000000000000))
print(countBits(100000000000000000000000000000))
print(countBits(1000000000000000000000000000000))
print(countBits(10000000000000000000000000000000))
print(count

if __name__ == '__main__':
    countBits()