def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    count = 10
    for i in range(2, n+1):
        temp = 9
        for j in range(1, i):
            temp *= (10-j)
        count += temp
    return count
print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(0))
