def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    ones, m = 0, 1
    while m <= n:
        ones += (n // m + 8) // 10 * m + (n // m % 10 == 1) * (n % m + 1)
        m *= 10
    return ones

if __name__ == '__main__':
    countDigitOne()