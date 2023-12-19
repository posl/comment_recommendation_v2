def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n > 10:
        n = 10
    total = 10
    for i in range(2,n+1):
        total += 9 * math.factorial(9) // math.factorial(9-i+1)
    return total
print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(0))
print(countNumbersWithUniqueDigits(3))
