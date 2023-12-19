def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    elif n == 1:
        return 10
    elif n == 2:
        return 91
    else:
        return countNumbersWithUniqueDigits(n-1) + (countNumbersWithUniqueDigits(n-1) - countNumbersWithUniqueDigits(n-2))*(10-n+1)
print(countNumbersWithUniqueDigits(3))
