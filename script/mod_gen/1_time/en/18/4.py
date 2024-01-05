def countNumbersWithUniqueDigits(n):
    if n == 0: return 1
    if n == 1: return 10
    if n > 10: return 0
    res = 10
    for i in range(2, n+1):
        tmp = 9
        for j in range(9, 9-i+1, -1):
            tmp *= j
        res += tmp
    return res

if __name__ == '__main__':
    n = int(input())
    a = countNumbersWithUniqueDigits(n)
    print(a)