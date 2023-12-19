def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    ans = [0]
    for i in range(1, n+1):
        ans.append(ans[i>>1] + (i & 1))
    return ans

if __name__ == '__main__':
    countBits()