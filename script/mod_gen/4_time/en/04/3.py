def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    return [bin(i).count('1') for i in range(n+1)]

if __name__ == '__main__':
    countBits()