def integerReplacement(n):
    """
    :type n: int
    :rtype: int
    """
    # if n is even, divide by 2
    # if n is odd, add or subtract 1
    # return the minimum number of operations to get to 1
    # 1 <= n <= 2^31 - 1
    # base case
    if n == 1:
        return 0
    # recursive case
    if n % 2 == 0:
        return 1 + integerReplacement(n / 2)
    else:
        return 1 + min(integerReplacement(n + 1), integerReplacement(n - 1))

if __name__ == '__main__':
    n = int(input())
    a = integerReplacement(n)
    print(a)