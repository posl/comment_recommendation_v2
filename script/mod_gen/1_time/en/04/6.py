def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    ans = []
    for i in range(n+1):
        ans.append(bin(i).count('1'))
    return ans

if __name__ == '__main__':
    countBits()