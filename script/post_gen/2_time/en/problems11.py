Synthesizing 10/10 solutions

=======
Suggestion 1

def lengthOfLIS(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))
nums = [0,1,0,3,2,3]
print(lengthOfLIS(nums))
nums = [7,7,7,7,7,7,7]
print(lengthOfLIS(nums))

=======
Suggestion 2

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 2:
        return len(nums)
    dp = [0] * len(nums)
    dp[0] = 1
    for i in range(1, len(nums)):
        maxval = 0
        for j in range(0, i):
            if nums[i] > nums[j]:
                maxval = max(maxval, dp[j])
        dp[i] = maxval + 1
    return max(dp)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))

=======
Suggestion 3

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
    
    return max(dp)
    
print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))

=======
Suggestion 4

def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))

=======
Suggestion 5

def lengthOfLIS(nums):
    n = len(nums)
    if n == 0:
        return 0
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

=======
Suggestion 6

def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0
    
    dp = [1 for _ in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

=======
Suggestion 7

def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0
    dp = [1 for i in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))

=======
Suggestion 8

def longestIncreasingSubsequence(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(dp)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

=======
Suggestion 9

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 1:
        return len(nums)
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

=======
Suggestion 10

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 2:
        return len(nums)
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)
