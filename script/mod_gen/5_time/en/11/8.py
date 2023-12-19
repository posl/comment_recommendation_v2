def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 2: return len(nums)
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
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
nums = [1,3,6,7,9,4,10,5,6]
print(lengthOfLIS(nums))
nums = [1,3,6,7,9,4,10,5,6]
print(lengthOfLIS(nums))
nums = [0,1,0,3,2,3]
print(lengthOfLIS(nums))
nums = [7,7,7,7,7,7,7]
print(lengthOfLIS(nums))
nums = [1,3,6,7,9,4,10,5,6]
print(lengthOfLIS(nums))
nums = [1,3,6,7,9,4,10,5,6]
print(lengthOfLIS(nums))
nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))
nums = [0,1,0,3,2,3]
print(lengthOfLIS(nums))
nums = [7,7,7,7,7,7,7]
print(lengthOfLIS(nums))
nums = [1,3,6,7,9,4,10,5,6]
print(lengthOfLIS(nums))
nums = [1,3,6,7,9,4,10,5,6]
print(lengthOfLIS(nums))
nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))
nums = [0,1,0,3,2,3]
print(lengthOfLIS(nums))
