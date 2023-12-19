def countNumbersWithUniqueDigits(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 1
    elif n == 1:
        return 10
    else:
        result = 10
        for i in range(2, n+1):
            temp = 9
            for j in range(9, 9-i+1, -1):
                temp *= j
            result += temp
        return result
print(countNumbersWithUniqueDigits(3))
