def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    result = []
    for i in range(n+1):
        result.append(bin(i).count('1'))
    return result
print(countBits(2))
print(countBits(5))
print(countBits(0))
print(countBits(1))
print(countBits(10))
