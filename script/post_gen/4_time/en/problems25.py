Synthesizing 10/10 solutions

=======
Suggestion 1

def maxCoins(nums):
    pass

print(maxCoins([3,1,5,8]))
print(maxCoins([1,5]))
print(maxCoins([1]))

=======
Suggestion 2

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
                dp[left][right] = max(dp[left][right],
                                      nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
    return dp[0][n - 1]

=======
Suggestion 3

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    def dp(i, j):
        if i + 1 == j: return 0
        if (i, j) in memo: return memo[(i, j)]
        memo[(i, j)] = max(nums[i] * nums[k] * nums[j] + dp(i, k) + dp(k, j) for k in range(i + 1, j))
        return memo[(i, j)]
    nums = [1] + nums + [1]
    memo = {}
    return dp(0, len(nums) - 1)

nums = [3,1,5,8]
print(maxCoins(nums))
nums = [1,5]
print(maxCoins(nums))

=======
Suggestion 4

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    nums = [1] + nums + [1]
    dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
    for l in range(1, n+1):
        for i in range(1, n-l+2):
            j = i+l-1
            for k in range(i, j+1):
                dp[i][j] = max(dp[i][j], dp[i][k-1]+nums[i-1]*nums[k]*nums[j+1]+dp[k+1][j])
    return dp[1][n]

print(maxCoins([3,1,5,8]))
print(maxCoins([1,5]))

=======
Suggestion 5

def maxCoins(nums):
    n = len(nums)
    nums = [1] + nums + [1]
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    for l in range(1, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            for k in range(i, j + 1):
                dp[i][j] = max(dp[i][j], dp[i][k - 1] + nums[i - 1] * nums[k] * nums[j + 1] + dp[k + 1][j])
    return dp[1][n]

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
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for length in range(2, n):
        for left in range(n - length):
            right = left + length
            for i in range(left + 1, right):
                dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])

    return dp[0][n - 1]

=======
Suggestion 7

def maxCoins(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n-1):
        dp[i][i+1] = 0
    for k in range(2, n):
        for left in range(n-k):
            right = left + k
            for i in range(left+1, right):
                dp[left][right] = max(dp[left][right], dp[left][i] + dp[i][right] + nums[left] * nums[i] * nums[right])
    return dp[0][n-1]

print(maxCoins([3,1,5,8]))
print(maxCoins([1,5]))
print(maxCoins([2,3,4,5,6,7,8,9]))
print(maxCoins([1,2,3,4,5,6,7,8,9,10]))
print("The values above should be 167, 10, 2010, and 14540.")

=======
Suggestion 8

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    nums = [1] + nums + [1]
    dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
    for l in range(1, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            for k in range(i, j+1):
                dp[i][j] = max(dp[i][j], dp[i][k-1] + nums[i-1] * nums[k] * nums[j+1] + dp[k+1][j])
    return dp[1][n]

=======
Suggestion 9

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0]*nums[1] + nums[1], nums[0] + nums[1]*nums[0])
    else:
        max_coins = 0
        for i in range(len(nums)):
            if i == 0:
                max_coins = max_coins + nums[i]*nums[i+1] + maxCoins(nums[i+1:])
            elif i == len(nums)-1:
                max_coins = max_coins + nums[i-1]*nums[i] + maxCoins(nums[:i])
            else:
                max_coins = max_coins + nums[i-1]*nums[i]*nums[i+1] + maxCoins(nums[:i] + nums[i+1:])
    return max_coins

print(maxCoins([3,1,5,8]))
print(maxCoins([1,5]))
print(maxCoins([1,2,3,4,5,6,7,8,9,10]))
print(maxCoins([1,2,3,4,5,6,7,8,9,10,11]))
print(maxCoins([1,2,3,4,5,6,7,8,9,10,11,12]))
print(maxCoins([1,2,3,4,5,6,7,8,9,10,11,12,13]))
print(maxCoins([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
print(maxCoins([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(maxCoins([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
print(maxCoins([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]))
print(maxCoins([1,2,3,4,5,6,7,8,9,10,11,12,13

=======
Suggestion 10

def maxCoins(nums):
    def dfs(nums, cache, left, right):
        if left + 1 == right:
            return 0
        if cache[left][right] > 0:
            return cache[left][right]
        result = 0
        for i in range(left + 1, right):
            result = max(result, nums[left] * nums[i] * nums[right] + dfs(nums, cache, left, i) + dfs(nums, cache, i, right))
        cache[left][right] = result
        return result
    nums = [1] + nums + [1]
    cache = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    return dfs(nums, cache, 0, len(nums) - 1)

print(maxCoins([3,1,5,8]))
print(maxCoins([1,5]))
