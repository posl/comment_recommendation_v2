Synthesizing 10/10 solutions

=======
Suggestion 1

def maxCoins(nums):
    n = len(nums)
    nums = [1] + nums + [1]
    dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

    for l in range(1, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            for k in range(i, j + 1):
                dp[i][j] = max(dp[i][j],
                               dp[i][k - 1] + nums[i - 1] * nums[k] * nums[j + 1] + dp[k + 1][j])

    return dp[1][n]

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

    for left in range(n - 2, -1, -1):
        for right in range(left + 2, n):
            for i in range(left + 1, right):
                dp[left][right] = max(dp[left][right],
                                      nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])

    return dp[0][n - 1]

=======
Suggestion 3

def maxCoins(nums):
    # Approach 1: Dynamic Programming
    # Time Complexity: O(n^3)
    # Space Complexity: O(n^2)
    # dp[i][j] = max(dp[i][j], dp[i][k-1] + nums[i-1]*nums[k]*nums[j+1] + dp[k+1][j])
    # dp[i][j] = max(dp[i][j], dp[i][k-1] + dp[k+1][j] + nums[i-1]*nums[k]*nums[j+1])

    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for length in range(1, n - 1):
        for i in range(1, n - length):
            j = i + length - 1
            for k in range(i, j + 1):
                dp[i][j] = max(dp[i][j], dp[i][k - 1] + dp[k + 1][j] + nums[i - 1] * nums[k] * nums[j + 1])

    return dp[1][n - 2]

nums = [3,1,5,8]
print(maxCoins(nums))

=======
Suggestion 4

def maxCoins(nums):
    # Fill this in.
    n = len(nums)
    nums.insert(0, 1)
    nums.append(1)
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    for l in range(1, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            for k in range(i, j + 1):
                dp[i][j] = max(dp[i][j], dp[i][k - 1] + nums[i - 1] * nums[k] * nums[j + 1] + dp[k + 1][j])
    return dp[1][n]

print(maxCoins([3, 1, 5, 8]))
# 167
print(maxCoins([1, 5]))
# 10

=======
Suggestion 5

def maxCoins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for gap in range(2, n):
        for left in range(0, n - gap):
            right = left + gap
            for i in range(left + 1, right):
                dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
    return dp[0][n - 1]

=======
Suggestion 6

def solution(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 2, -1, -1):
        for j in range(i + 2, n):
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
    return dp[0][n - 1]

=======
Suggestion 7

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # dp[i][j] = max coins from bursting all the balloons in nums[i:j+1]
    # dp[i][j] = max(dp[i][k-1] + dp[k+1][j] + nums[i-1]*nums[k]*nums[j+1]) for k in range(i,j+1)
    # dp[i][i] = nums[i-1]*nums[i]*nums[i+1]
    # dp[i][i+1] = max(dp[i][i] + dp[i+1][i+1] + nums[i-1]*nums[i]*nums[i+1],
    #                  dp[i][i] + dp[i+2][i+1] + nums[i-1]*nums[i+1]*nums[i+2])
    # dp[i][i+2] = max(dp[i][i+1] + dp[i+2][i+2] + nums[i-1]*nums[i]*nums[i+2],
    #                  dp[i][i+1] + dp[i+3][i+2] + nums[i-1]*nums[i+2]*nums[i+3],
    #                  dp[i][i] + dp[i+2][i+2] + nums[i-1]*nums[i]*nums[i+2],
    #                  dp[i][i] + dp[i+3][i+2] + nums[i-1]*nums[i+2]*nums[i+3])
    # dp[i][i+3] = max(dp[i][i+2] + dp[i+3][i+3] + nums[i-1]*nums[i]*nums[i+3],
    #                  dp[i][i+2] + dp[i+4][i+3] + nums[i-1]*nums[i+3]*nums[i+4],
    #                  dp[i][i+1] + dp[i+3][i+3] + nums[i-1]*nums[i]*nums[i+3],
    #                  dp[i][i+1] + dp[i+4][i+3] + nums[i-1]*nums[i+3]*nums[i+4])
    # dp[i][i+4] = max(dp[i][i+3] + dp[i+

=======
Suggestion 8

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0 for j in range(n)] for i in range(n)]

    for l in range(2, n):
        for i in range(0, n - l):
            j = i + l
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])

    return dp[0][n - 1]

print(maxCoins([3,1,5,8]))
print(maxCoins([1,5]))
print(maxCoins([1,5,7,9]))
print(maxCoins([1,5,8,9,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,7,8,9,1,2,3,4,5,6,7,8,9]))
print("The values above should be 167, 10, 516, and 1750.")

=======
Suggestion 9

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations
    #https://www.youtube.com/watch?v=IFNibRVgFBo
    #https://www.youtube.com/watch?v=ASoaQq66foQ
    #https://www.youtube.com/watch?v=IFNibRVgFBo
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0]*n for _ in range(n)]
    #dp[i][j] = max coins in nums[i:j]
    for l in range(2, n): #length of subarray
        for i in range(n-l): #start index
            j = i + l #end index
            for k in range(i+1, j): #burst index
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j])
    return dp[0][n-1]

=======
Suggestion 10

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0]*nums[1]+nums[1], nums[0]*nums[1]+nums[0])
    if len(nums) == 3:
        return max(nums[0]*nums[1]*nums[2]+nums[0]*nums[2]+nums[1], nums[0]*nums[1]*nums[2]+nums[0]*nums[1]+nums[2], nums[0]*nums[1]*nums[2]+nums[1]*nums[2]+nums[0])
    else:
        max_coins = 0
        for i in range(len(nums)):
            if i == 0:
                max_coins = max(max_coins, nums[i]*nums[i+1]*nums[i+2]+maxCoins(nums[i+2:]))
            elif i == len(nums)-1:
                max_coins = max(max_coins, nums[i-1]*nums[i]*nums[i+1]+maxCoins(nums[:i-1]))
            else:
                max_coins = max(max_coins, nums[i-1]*nums[i]*nums[i+1]+maxCoins(nums[:i-1]+nums[i+2:]))
        return max_coins

print(maxCoins([3,1,5,8]))
print(maxCoins([
