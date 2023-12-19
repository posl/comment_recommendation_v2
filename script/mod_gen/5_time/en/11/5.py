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
                dp[i] = max(dp[i], 1 + dp[j])
                
    return max(dp)
print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))
print(lengthOfLIS([0]))
print(lengthOfLIS([]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
print(lengthOfLIS([4,10,4,3,8,9]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))
print(lengthOfLIS([0]))
print(lengthOfLIS([]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
print(lengthOfLIS([4,10,4,3,8,9]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))
print(lengthOfLIS([0]))
print(lengthOfLIS([])))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
print(lengthOfLIS([4,10,4,3,8,9]))
print(lengthOfLIS([1,
