def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    res = [0]
    for i in range(1, n+1):
        res.append(res[i>>1] + (i&1))
    return res
print(countBits(5))
