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

if __name__ == '__main__':
    countNumbersWithUniqueDigits()