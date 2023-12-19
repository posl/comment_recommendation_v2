def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    ans = []
    for i in range(n+1):
        ans.append(bin(i).count('1'))
    return ans
n = 5
print(countBits(n))
