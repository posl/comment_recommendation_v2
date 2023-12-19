def integerBreak(n):
    if n <= 3:
        return n - 1
    else:
        count = 0
        while n > 4:
            n -= 3
            count += 1
        return 3 ** count * n
print(integerBreak(10))
