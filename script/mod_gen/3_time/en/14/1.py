def integerBreak(n):
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 4
    result = 1
    while n > 4:
        result *= 3
        n -= 3
    result *= n
    return result
print(integerBreak(10))
