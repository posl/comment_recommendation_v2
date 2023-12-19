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
