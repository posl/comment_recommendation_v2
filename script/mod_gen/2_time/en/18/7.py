def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    elif n == 1:
        return 10
    elif n == 2:
        return 91
    else:
        count = 91
        for i in range(3, n+1):
            count += 9 * (10 - i + 1) * (10 - i + 1)
        return count
print(countNumbersWithUniqueDigits(3))
