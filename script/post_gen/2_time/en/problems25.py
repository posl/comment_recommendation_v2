Synthesizing 10/10 solutions

=======
Suggestion 1

def maxCoins(nums):
    # dp[i][j] is the max coins we can get by bursting all the balloons between i and j
    # dp[i][j] = max(dp[i][k-1] + dp[k+1][j] + nums[i-1] * nums[k] * nums[j+1]) for i <= k <= j
    # dp[i][j] = 0 if i > j
    # dp[i][i] = nums[i-1] * nums[i] * nums[i+1]
    # dp[i][i+1] = max(nums[i-1] * nums[i] * nums[i+1], nums[i] * nums[i+1] * nums[i+2])
    # dp[i][i+2] = max(nums[i-1] * nums[i] * nums[i+1] + nums[i-1] * nums[i+1] * nums[i+2], nums[i] * nums[i+1] * nums[i+2] + nums[i] * nums[i+2] * nums[i+3])
    # dp[i][i+3] = max(nums[i-1] * nums[i] * nums[i+1] + nums[i-1] * nums[i+1] * nums[i+2] + nums[i-1] * nums[i+2] * nums[i+3], nums[i] * nums[i+1] * nums[i+2] + nums[i] * nums[i+2] * nums[i+3] + nums[i] * nums[i+3] * nums[i+4])
    # dp[i][i+4] = max(nums[i-1] * nums[i] * nums[i+1] + nums[i-1] * nums[i+1] * nums[i+2] + nums[i-1] * nums[i+2] * nums[i+3] + nums[i-1] * nums[i+3] * nums[i+4], nums[i] * nums[i+1] * nums[i+2] + nums[i] * nums[i+2] * nums[i+3] + nums[i] * nums[i+3] * nums[i+4] + nums[i] * nums[i+4] * nums[i+5])
    # dp[i][i+5] = max(nums[i-1] * nums[i

=======
Suggestion 2

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 1. DP
    # dp[i][j] = max(dp[i][j], dp[i][k-1] + nums[i-1]*nums[k]*nums[j+1] + dp[k+1][j] for k in range(i, j+1))
    # Time: O(n^3)
    # Space: O(n^2)
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0]*n for _ in range(n)]
    for i in range(n-2, -1, -1):
        for j in range(i+2, n):
            for k in range(i+1, j):
                dp[i][j] = max(dp[i][j], dp[i][k-1] + nums[i]*nums[k]*nums[j] + dp[k+1][j])
    return dp[0][n-1]

=======
Suggestion 3

def maxCoins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0]*n for _ in range(n)]
    
    for length in range(2, n):
        for left in range(n - length):
            right = left + length
            for i in range(left + 1, right):
                dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
    return dp[0][n - 1]

=======
Suggestion 4

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for left in range(n - 2, -1, -1):
        for right in range(left + 2, n):
            for i in range(left + 1, right):
                dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])

    return dp[0][n - 1]

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
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            for k in range(i+1, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j])
    return dp[0][n-1]

print(maxCoins([3,1,5,8]))
print(maxCoins([1,5]))

=======
Suggestion 6

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Dynamic Programming Approach
    # Time Complexity: O(n^3)
    # Space Complexity: O(n^2)
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n-3, -1, -1):
        for j in range(i+2, n):
            for k in range(i+1, j):
                dp[i][j] = max(dp[i][j], nums[i]*nums[k]*nums[j] + dp[i][k] + dp[k][j])
                
    return dp[0][n-1]

=======
Suggestion 7

def maxCoins(nums):
    n = len(nums)
    dp = [[0]*n for _ in range(n)]
    for l in range(n):
        for i in range(n-l):
            j = i+l
            for k in range(i,j+1):
                left = 1
                right = 1
                if i != 0:
                    left = nums[i-1]
                if j != n-1:
                    right = nums[j+1]
                before = 0
                after = 0
                if k != i:
                    before = dp[i][k-1]
                if k != j:
                    after = dp[k+1][j]
                dp[i][j] = max(dp[i][j], before + left*nums[k]*right + after)
    return dp[0][n-1]

nums = [3,1,5,8]
print(maxCoins(nums))

=======
Suggestion 8

def maxCoins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0 for i in range(n)] for j in range(n)]
    for length in range(2, n):
        for left in range(0, n - length):
            right = left + length
            for i in range(left + 1, right):
                dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
    return dp[0][n - 1]

print(maxCoins([3,1,5,8]))
print(maxCoins([1,5]))

=======
Suggestion 9

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
    return dp[0][n - 1]

=======
Suggestion 10

def maxCoins(nums):
    n = len(nums)
    nums = [1] + nums + [1]
    dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
    for i in range(n, -1, -1):
        for j in range(i+1, n+2):
            for k in range(i+1, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
    return dp[0][n+1]
