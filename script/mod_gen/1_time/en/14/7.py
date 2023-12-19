def integerBreak(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 2:
        return 1
    elif n == 3:
        return 2
    elif n == 4:
        return 4
    elif n == 5:
        return 6
    elif n == 6:
        return 9
    else:
        return 3 * integerBreak(n - 3)

if __name__ == '__main__':
    integerBreak()