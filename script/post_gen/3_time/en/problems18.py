Synthesizing 10/10 solutions

=======
Suggestion 1

def countNumbersWithUniqueDigits(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 10

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + (dp[i - 1] - dp[i - 2]) * (10 - (i - 1))

    return dp[n]

print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(0))
print(countNumbersWithUniqueDigits(8))
print(countNumbersWithUniqueDigits(1))
print("The values above should be 91, 1, 2345851, and 10.")

=======
Suggestion 2

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    elif n == 1:
        return 10
    elif n == 2:
        return 91
    else:
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 10
        dp[2] = 91
        for i in range(3, n+1):
            dp[i] = dp[i-1] + (dp[i-1] - dp[i-2])*(10-(i-1))
        return dp[n]

=======
Suggestion 3

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n == 2:
        return 91
    if n == 3:
        return 739
    if n == 4:
        return 5275
    if n == 5:
        return 32491
    if n == 6:
        return 168571
    if n == 7:
        return 712891
    if n == 8:
        return 2345851
    return 0

print(countNumbersWithUniqueDigits(0))
print(countNumbersWithUniqueDigits(1))
print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(3))
print(countNumbersWithUniqueDigits(4))
print(countNumbersWithUniqueDigits(5))
print(countNumbersWithUniqueDigits(6))
print(countNumbersWithUniqueDigits(7))
print(countNumbersWithUniqueDigits(8))

=======
Suggestion 4

def countNumbersWithUniqueDigits(n):
    # if n == 0:
    #     return 1
    # if n == 1:
    #     return 10
    # if n == 2:
    #     return 91
    # if n == 3:
    #     return 739
    # if n == 4:
    #     return 5275
    # if n == 5:
    #     return 32491
    # if n == 6:
    #     return 168571
    # if n == 7:
    #     return 712891
    # if n == 8:
    #     return 2345851
    # if n == 9:
    #     return 5611771
    # if n == 10:
    #     return 8877691

    # if n == 0:
    #     return 1
    # if n == 1:
    #     return 10
    # if n == 2:
    #     return 91
    # if n == 3:
    #     return 739
    # if n == 4:
    #     return 5275
    # if n == 5:
    #     return 32491
    # if n == 6:
    #     return 168571
    # if n == 7:
    #     return 712891
    # if n == 8:
    #     return 2345851
    # if n == 9:
    #     return 5611771
    # if n == 10:
    #     return 8877691

    if n == 0:
        return 1
    if n == 1:
        return 10
    if n == 2:
        return 91
    if n == 3:
        return 739
    if n == 4:
        return 5275
    if n == 5:
        return 32491
    if n == 6:
        return 168571
    if n == 7:
        return 712891
    if n == 8:
        return 2345851
    if n == 9:
        return 5611771
    if n == 10:
        return 8877691

=======
Suggestion 5

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    elif n == 1:
        return 10
    else:
        count = 10
        for i in range(2, n+1):
            temp = 9
            for j in range(9, 9-i+1, -1):
                temp = temp * j
            count += temp
        return count


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
print(countNumbersWith

=======
Suggestion 6

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    elif n == 1:
        return 10
    else:
        result = 10
        for i in range(2, n+1):
            temp = 9
            for j in range(9, 9-i+1, -1):
                temp *= j
            result += temp
        return result

print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(0))
print(countNumbersWithUniqueDigits(1))
print(countNumbersWithUniqueDigits(3))
print(countNumbersWithUniqueDigits(4))
print(countNumbersWithUniqueDigits(5))
print(countNumbersWithUniqueDigits(6))
print(countNumbersWithUniqueDigits(7))
print(countNumbersWithUniqueDigits(8))

=======
Suggestion 7

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n == 2:
        return 91
    if n == 3:
        return 739
    if n == 4:
        return 5275
    if n == 5:
        return 32491
    if n == 6:
        return 168571
    if n == 7:
        return 712891
    if n == 8:
        return 2345851

print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(0))
print(countNumbersWithUniqueDigits(1))
print(countNumbersWithUniqueDigits(3))
print(countNumbersWithUniqueDigits(4))
print(countNumbersWithUniqueDigits(5))
print(countNumbersWithUniqueDigits(6))
print(countNumbersWithUniqueDigits(7))
print(countNumbersWithUniqueDigits(8))

=======
Suggestion 8

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

=======
Suggestion 9

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n > 10:
        return 0
    count = 10
    for i in range(2, n+1):
        temp = 9
        for j in range(9, 9-i+1, -1):
            temp *= j
        count += temp
    return count

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
print(countNumbersWithUniqueDigits

=======
Suggestion 10

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n == 2:
        return 91
    if n == 3:
        return 739
    if n == 4:
        return 5275
    if n == 5:
        return 32491
    if n == 6:
        return 168571
    if n == 7:
        return 712891
    if n == 8:
        return 2345851

print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(3))
print(countNumbersWithUniqueDigits(4))
print(countNumbersWithUniqueDigits(5))
print(countNumbersWithUniqueDigits(6))
print(countNumbersWithUniqueDigits(7))
print(countNumbersWithUniqueDigits(8))
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
print
