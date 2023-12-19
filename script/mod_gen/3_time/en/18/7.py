def uniqueDigits(n):
    if n == 0:
        return 1
    elif n == 1:
        return 10
    elif n == 2:
        return 91
    else:
        return (n-1)*9*9 + uniqueDigits(n-1)
print(uniqueDigits(2))
print(uniqueDigits(3))
print(uniqueDigits(4))
print(uniqueDigits(5))
print(uniqueDigits(6))
print(uniqueDigits(7))
print(uniqueDigits(8))
print(uniqueDigits(9))
print(uniqueDigits(10))
