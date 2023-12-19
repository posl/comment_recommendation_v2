def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    res = []
    for i in range(n+1):
        res.append(bin(i)[2:].count('1'))
    return res

if __name__ == '__main__':
    countBits()