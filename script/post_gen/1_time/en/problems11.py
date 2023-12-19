Synthesizing 10/10 solutions

=======
Suggestion 1

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # O(n^2) solution
    # dp[i] = length of longest increasing subsequence ending at index i
    # dp[i] = max(dp[j] + 1 for j in range(i) if nums[j] < nums[i])
    # return max(dp)
    
    # O(n log n) solution
    # tails[i] = smallest tail of all increasing subsequences of length i+1
    # tails[i] = min(tails[j] for j in range(i) if tails[j] >= nums[i])
    # return len(tails)
    
    tails = []
    for num in nums:
        i = bisect.bisect_left(tails, num)
        if i == len(tails):
            tails.append(num)
        else:
            tails[i] = num
    return len(tails)

=======
Suggestion 2

def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

=======
Suggestion 3

def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0
    dp = [1 for _ in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

=======
Suggestion 4

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
                dp[i] = max(dp[i], dp[j]+1)
    
    return max(dp)

=======
Suggestion 5

def lengthOfLIS(nums):
    if not nums:
        return 0
    dp = [1 for _ in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

=======
Suggestion 6

def lengthOfLIS(nums):
    dp = [1 for i in range(len(nums))]
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)

=======
Suggestion 7

def lengthOfLIS(nums):
    # Time: O(n^2)
    # Space: O(n)
    # dp[i] = length of longest increasing subsequence ending at index i
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)

=======
Suggestion 8

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    dp = [1]*len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

=======
Suggestion 9

def lengthOfLIS(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

=======
Suggestion 10

def lengthOfLIS(nums):
    dp = [1]*len(nums)
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i]>nums[j]:
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
