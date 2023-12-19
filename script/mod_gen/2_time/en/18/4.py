def uniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n > 10:
        return 0
    count = 0
    for i in range(10**n):
        if len(str(i)) == len(set(str(i))):
            count += 1
    return count
print(uniqueDigits(2))
print(uniqueDigits(0))
print(uniqueDigits(1))
print(uniqueDigits(3))
print(uniqueDigits(4))
print(uniqueDigits(5))
print(uniqueDigits(6))
print(uniqueDigits(7))
print(uniqueDigits(8))
print(uniqueDigits(9))
print(uniqueDigits(10))
print(uniqueDigits(11))
print(uniqueDigits(12))
print(uniqueDigits(13))
print(uniqueDigits(14))
print(uniqueDigits(15))
print(uniqueDigits(16))
print(uniqueDigits(17))
print(uniqueDigits(18))
print(uniqueDigits(19))
print(uniqueDigits(20))
