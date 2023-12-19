def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    n = len(nums)
    dp = [[float('inf') for _ in range(m+1)] for _ in range(n+1)]
    sub = [0]
    for num in nums:
        sub.append(sub[-1] + num)
    dp[0][0] = 0
    for i in range(1, n+1):
        for j in range(1, min(m, i)+1):
            for k in range(i):
                dp[i][j] = min(dp[i][j], max(dp[k][j-1], sub[i]-sub[k]))
    return dp[n][m]
print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
print(splitArray([1,4,4], 3))
print(splitArray([1,2,3,4,5], 4))
print(splitArray([1,2,3,4,5], 5))
print(splitArray([1,2,3,4,5], 6))
print(splitArray([1,2,3,4,5], 7))
print(splitArray([1,2,3,4,5,6], 7))
print(splitArray([1,2,3,4,5,6], 6))
print(splitArray([1,2,3,4,5,6], 5))
print(splitArray([1,2,3,4,5,6], 4))
print(splitArray([1,2,3,4,5,6], 3))
print(splitArray([1,2,3,4,5,6], 2))
print(splitArray([1,2,3,4,5,6], 1))
print(splitArray([1,2,3,4,5,6], 0))
print(splitArray([1,2,3,4,5,6], 8))
print(splitArray([1,2,3,4,5,6], 9))
print(splitArray([1,2,3,4,5,6], 10))
print(splitArray([1,2,3,4,5,
