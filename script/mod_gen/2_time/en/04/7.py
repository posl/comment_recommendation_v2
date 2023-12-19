def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    #return [bin(i).count('1') for i in range(n+1)]
    return [bin(i).count('1') for i in range(n+1)]
print(countBits(2))
print(countBits(5))
