def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    res = [0]
    for i in range(1, n+1):
        res.append(res[i >> 1] + i % 2)
    return res

if __name__ == '__main__':
    countBits()