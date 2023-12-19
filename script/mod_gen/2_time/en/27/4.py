def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    for i in range(1,n+1):
        count += str(i).count('1')
    return count
countDigitOne(13)
