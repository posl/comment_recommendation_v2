def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    dp = [[num] for num in nums]
    res = []
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [nums[i]]
        if len(res) < len(dp[i]):
            res = dp[i]
    return res
print(largestDivisibleSubset([1,2,3]))
