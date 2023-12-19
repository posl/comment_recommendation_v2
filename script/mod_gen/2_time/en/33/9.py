def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    dp = [collections.defaultdict(int) for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(i):
            dp[i][nums[i] - nums[j]] += 1
            if nums[i] - nums[j] in dp[j]:
                dp[i][nums[i] - nums[j]] += dp[j][nums[i] - nums[j]]
                res += dp[j][nums[i] - nums[j]]
    return res
nums = [2,4,6,8,10]
print(numberOfArithmeticSlices(nums))
nums = [7,7,7,7,7]
print(numberOfArithmeticSlices(nums))
