def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    res = 10
    uniqueDigits = 9
    availableNumber = 9
    while n > 1 and availableNumber > 0:
        uniqueDigits = uniqueDigits * availableNumber
        res += uniqueDigits
        availableNumber -= 1
        n -= 1
    return res
print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(0))
print(countNumbersWithUniqueDigits(8))
print(countNumbersWithUniqueDigits(6))
print(countNumbersWithUniqueDigits(5))
print(countNumbersWithUniqueDigits(4))
print(countNumbersWithUniqueDigits(3))
print(countNumbersWithUniqueDigits(9))
print(countNumbersWithUniqueDigits(10))
print(countNumbersWithUniqueDigits(11))
print(countNumbersWithUniqueDigits(12))
print(countNumbersWithUniqueDigits(13))
print(countNumbersWithUniqueDigits(14))
print(countNumbersWithUniqueDigits(15))
print(countNumbersWithUniqueDigits(16))
print(countNumbersWithUniqueDigits(17))
print(countNumbersWithUniqueDigits(18))
print(countNumbersWithUniqueDigits(19))
print(countNumbersWithUniqueDigits(20))
print(countNumbersWithUniqueDigits(21))
print(countNumbersWithUniqueDigits(22))
print(countNumbersWithUniqueDigits(23))
print(countNumbersWithUniqueDigits(24))
print(countNumbersWithUniqueDigits(25))
print(countNumbersWithUniqueDigits(26))
print(countNumbersWithUniqueDigits(27))
print(countNumbersWithUniqueDigits(28))
print(countNumbersWithUniqueDigits(29))
print(countNumbersWithUniqueDigits(30))
print(countNumbersWithUniqueDigits(31))
print(countNumbersWithUniqueDigits(32))
print(countNumbersWithUniqueDigits(33))
print(countNumbersWithUniqueDigits(34))
print(countNumbersWithUniqueDigits(35))
print(countNumbersWithUniqueDigits(36))
print(countNumbersWithUniqueDigits(37))
print(countNumbersWithUniqueDigits(38))
print(countNumbersWithUniqueDigits(39))
print(countNumbersWithUniqueDigits(40))
print(countNumbersWithUniqueDigits(41))
print(countNumbersWithUniqueDigits(42))
print(countNumbersWithUniqueDigits(43))
print(countNumbersWithUniqueDigits(44))
print(countNumbersWithUniqueDigits(45))
print(countNumbersWithUniqueDigits(46))
print(countNumbersWithUniqueDigits(47))
print

if __name__ == '__main__':
    countNumbersWithUniqueDigits()