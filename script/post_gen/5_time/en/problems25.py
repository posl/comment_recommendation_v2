Synthesizing 10/10 solutions

=======
Suggestion 1

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for k in range(2, n):
        for left in range(0, n - k):
            right = left + k
            for i in range(left + 1, right):
                dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
    return dp[0][n - 1]

nums = [3,1,5,8]
print(maxCoins(nums))

=======
Suggestion 2

def maxCoins(nums):
    n = len(nums)
    nums = [1] + nums + [1]
    dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
    for i in range(n-1, -1, -1):
        for j in range(i+2, n+2):
            for k in range(i+1, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j])
    return dp[0][n+1]

print(maxCoins([3,1,5,8]))
print(maxCoins([1,5]))

=======
Suggestion 3

def maxCoins(nums):
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0]*nums[1]+nums[0], nums[0]*nums[1]+nums[1])
    else:
        max_coins = 0
        for i in range(len(nums)):
            if i == 0:
                max_coins = max(max_coins, nums[i]*nums[i+1] + maxCoins(nums[i+1:]))
            elif i == len(nums)-1:
                max_coins = max(max_coins, nums[i]*nums[i-1] + maxCoins(nums[:i]))
            else:
                max_coins = max(max_coins, nums[i-1]*nums[i]*nums[i+1] + maxCoins(nums[:i]+nums[i+1:]))
        return max_coins

nums = [3,1,5,8]
print(maxCoins(nums))

=======
Suggestion 4

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # dp[i][j] = max(dp[i][k-1] + nums[i-1]*nums[k]*nums[j+1] + dp[k+1][j]) where i <= k <= j
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0]*n for _ in range(n)]
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            for k in range(i+1, j):
                dp[i][j] = max(dp[i][j], dp[i][k-1] + nums[i]*nums[k]*nums[j] + dp[k+1][j])
    return dp[0][n-1]

print(maxCoins([3,1,5,8]))

=======
Suggestion 5

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for gap in range(2, n):
        for i in range(n - gap):
            j = i + gap
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])

    return dp[0][n - 1]

print(maxCoins([3,1,5,8]))
print(maxCoins([1,5]))

=======
Suggestion 6

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for i in range(n-2, -1, -1):
        for j in range(i+2, n):
            for k in range(i+1, j):
                dp[i][j] = max(dp[i][j], nums[i]*nums[k]*nums[j] + dp[i][k] + dp[k][j])
    return dp[0][n-1]

print(maxCoins([3,1,5,8]))
print(maxCoins([1,5]))
print(maxCoins([1,3,5,8]))
print(maxCoins([9,76,64,21,97,60,5]))
print(maxCoins([2,4,8,4,0,7,8,9,1,2,4,5,0,6,7,8,9,4,3,2,1,2,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,0,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9]))

=======
Suggestion 7

def maxCoins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0]*n for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            for k in range(i+1, j):
                dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])
    return dp[0][n-1]

=======
Suggestion 8

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(2, n):
        for j in range(n - i):
            for k in range(j + 1, j + i):
                dp[j][j + i] = max(dp[j][j + i], nums[j] * nums[k] * nums[j + i] + dp[j][k] + dp[k][j + i])
    return dp[0][n - 1]

=======
Suggestion 9

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations
    #https://www.youtube.com/watch?v=IFNibRVgFBo
    #https://www.youtube.com/watch?v=z3hu2Be92UA
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=ASoaQq66foQ
    #https://www.youtube.com/watch?v=IFNibRVgFBo
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=ASoaQq66foQ
    #https://www.youtube.com/watch?v=IFNibRVgFBo
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=ASoaQq66foQ
    #https://www.youtube.com/watch?v=IFNibRVgFBo
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=ASoaQq66foQ
    #https://www.youtube.com/watch?v=IFNibRVgFBo
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=ASoaQq66foQ
    #https://www.youtube.com/watch?v=IFNibRVgFBo
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=ASoaQq66foQ
    #https://www.youtube.com/watch?v=IFNibRVgFBo
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=ASoaQq66foQ
    #https://www.youtube.com/watch?v=IFNibRVgFBo
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=ASoaQq66foQ

    #

=======
Suggestion 10

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])

    return dp[0][n - 1]

print(maxCoins([3,1,5,8]))
print(maxCoins([1,5]))
