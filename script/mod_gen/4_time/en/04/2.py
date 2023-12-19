def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    #return [bin(i).count('1') for i in range(n+1)] # list comprehension
    ans = [0 for i in range(n+1)]
    for i in range(n+1):
        ans[i] = ans[i//2] + i%2
    return ans

if __name__ == '__main__':
    countBits()