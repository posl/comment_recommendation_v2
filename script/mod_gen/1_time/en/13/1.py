def integerReplacement(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + integerReplacement(n // 2)
    else:
        return 1 + min(integerReplacement(n + 1), integerReplacement(n - 1))
    
#Test Cases
integerReplacement(8) #3
integerReplacement(7) #4
integerReplacement(4) #2
