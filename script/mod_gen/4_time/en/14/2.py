def integerBreak(n):
    # if n <= 3:
    #     return n - 1
    # else:
    #     return 3 ** (n // 3) * (n % 3 or 1)
    if n <= 3:
        return n - 1
    else:
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n
print(integerBreak(10))
