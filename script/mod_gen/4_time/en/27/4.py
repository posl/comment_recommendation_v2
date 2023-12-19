def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 1:
        return 0
    count = 0
    for i in range(1, n+1):
        while i > 0:
            if i % 10 == 1:
                count += 1
            i //= 10
    return count

if __name__ == '__main__':
    countDigitOne()