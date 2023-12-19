def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    result = [0] * (n+1)
    for i in range(n+1):
        result[i] = result[i//2] + i%2
    return result
print(countBits(2))
print(countBits(5))
