Synthesizing 10/10 solutions

=======
Suggestion 1

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # O(n^2) - Dynamic Programming
    # O(n) - Binary Search
    # The idea is to use an array to store the longest increasing subsequence
    # so far. The array is sorted from small to large. For each new item, we
    # do binary search to find the first item in the array which is larger than
    # the new item. If there is no such item, we append the new item to the
    # array. Otherwise, we replace the first item which is larger than the new
    # item with the new item.
    # The size of the array is the length of the longest increasing subsequence
    # so far.
    # Reference: https://www.youtube.com/watch?v=1RpMc3fv0y4
    # Time: O(nlogn)
    # Space: O(n)
    if not nums:
        return 0

    dp = []
    for num in nums:
        if not dp or num > dp[-1]:
            dp.append(num)
        else:
            left = 0
            right = len(dp) - 1
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            dp[left] = num
    return len(dp)

=======
Suggestion 2

def lengthOfLIS(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1
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
    # O(n^2) solution
    # dp = [1] * len(nums)
    # for i in range(len(nums)):
    #     for j in range(i):
    #         if nums[i] > nums[j]:
    #             dp[i] = max(dp[i], dp[j] + 1)
    # return max(dp)
    
    # O(n log n) solution
    dp = []
    for num in nums:
        idx = bisect.bisect_left(dp, num)
        if idx == len(dp):
            dp.append(num)
        else:
            dp[idx] = num
    return len(dp)

=======
Suggestion 4

def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0
    dp = [1] * len(nums)
    for i in range(1,len(nums)):
        for j in range(0,i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

=======
Suggestion 5

def longestIncreasingSubsequence(nums):
    if len(nums) == 0:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

=======
Suggestion 6

def lengthOfLIS(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))

=======
Suggestion 7

def lengthOfLIS(nums):
    if len(nums) == 1:
        return 1
    if len(nums) == 0:
        return 0

    dp = [1] * len(nums)
    maxLen = 1

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
                maxLen = max(maxLen, dp[i])

    return maxLen

=======
Suggestion 8

def lengthOfLIS(self, nums: List[int]) -> int:
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp) if dp else 0

=======
Suggestion 9

def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0
    dp = [1 for i in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(0, i):
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
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))
