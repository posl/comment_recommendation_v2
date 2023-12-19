def integerBreak(n):
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n % 3 == 0:
        return pow(3, n // 3)
    if n % 3 == 1:
        return 4 * pow(3, (n - 4) // 3)
    return 2 * pow(3, n // 3)
print(integerBreak(10))
