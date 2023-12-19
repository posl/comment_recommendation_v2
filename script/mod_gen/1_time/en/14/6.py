def integerBreak(n):
    if n <= 3:
        return n - 1
    product = 1
    while n > 4:
        product *= 3
        n -= 3
    product *= n
    return product

if __name__ == '__main__':
    integerBreak()