def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    elif n == 1:
        return 10
    elif n == 2:
        return 91
    else:
        return 91 + countNumbersWithUniqueDigits(n-1) - countNumbersWithUniqueDigits(n-2)
print(countNumbersWithUniqueDigits(0))
print(countNumbersWithUniqueDigits(1))
print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(3))
print(countNumbersWithUniqueDigits(4))
print(countNumbersWithUniqueDigits(5))
print(countNumbersWithUniqueDigits(6))
print(countNumbersWithUniqueDigits(7))
print(countNumbersWithUniqueDigits(8))
