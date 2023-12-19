def minOperations(n):
    """
    :type n: int
    :rtype: int
    """
    operations = 0
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = n - 1
        operations += 1
    return operations

if __name__ == '__main__':
    minOperations()