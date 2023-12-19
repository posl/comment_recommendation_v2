def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    elif n == 1:
        return 10
    else:
        ans = 10
        for i in range(2, n+1):
            product = 9
            for j in range(9, 9-i+1, -1):
                product *= j
            ans += product
        return ans
print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(0))
print(countNumbersWithUniqueDigits(1))
print(countNumbersWithUniqueDigits(3))
print(countNumbersWithUniqueDigits(4))
print(countNumbersWithUniqueDigits(5))
print(countNumbersWithUniqueDigits(6))
print(countNumbersWithUniqueDigits(7))
print(countNumbersWithUniqueDigits(8))
print(countNumbersWithUniqueDigits(9))
print(countNumbersWithUniqueDigits(10))
print(countNumbersWithUniqueDigits(11))
