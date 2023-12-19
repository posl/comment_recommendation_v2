def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    ans = [0]*(n+1)
    for i in range(1,n+1):
        ans[i] = ans[i&(i-1)] + 1
    return ans
print(countBits(5))
