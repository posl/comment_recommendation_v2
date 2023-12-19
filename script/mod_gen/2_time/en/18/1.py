def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n == 2:
        return 91
    res = 91
    for i in range(3, n+1):
        res += 9*9*10**(i-2)
    return res

if __name__ == '__main__':
    countNumbersWithUniqueDigits()