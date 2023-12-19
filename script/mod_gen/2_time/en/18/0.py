def countNumbersWithUniqueDigits(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 1
    res = 10
    uniqueDigits = 9
    availableNumber = 9
    while n > 1 and availableNumber > 0:
        uniqueDigits = uniqueDigits * availableNumber
        res += uniqueDigits
        availableNumber -= 1
        n -= 1
    return res

if __name__ == '__main__':
    countNumbersWithUniqueDigits()