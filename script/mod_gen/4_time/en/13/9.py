def integerReplacement(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            count += 1
        elif n == 3 or n % 4 == 1:
            n -= 1
            count += 1
        else:
            n += 1
            count += 1
    return count
print(integerReplacement(8))
print(integerReplacement(7))
print(integerReplacement(4))
print(integerReplacement(15))
print(integerReplacement(100000000))
