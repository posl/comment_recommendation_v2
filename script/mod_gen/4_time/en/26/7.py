def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    n = len(nums)
    dp = [[float('inf') for _ in range(n+1)] for _ in range(m+1)]
    dp[0][0] = 0
    sub = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        sub[i] = sub[i-1] + nums[i-1]
    for i in range(1, m+1):
        for j in range(i, n+1):
            for k in range(i-1, j):
                dp[i][j] = min(dp[i][j], max(dp[i-1][k], sub[j] - sub[k]))
    return dp[m][n]
print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
print(splitArray([1,4,4], 3))
print(splitArray([1,2,3,4,5], 3))
print(splitArray([1,2147483647], 2))
print(splitArray([1,2,3,4,5], 1))
print(splitArray([1,2,3,4,5], 5))
print("The values above should be 18, 9, 4, 6, 2147483647, 15, 5, and 5.")

if __name__ == '__main__':
    splitArray()