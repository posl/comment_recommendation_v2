def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    ans = 0
    dp = [{} for _ in range(n)]
    for i in range(n):
        for j in range(i):
            d = nums[i] - nums[j]
            dp[i][d] = dp[i].get(d, 0) + dp[j].get(d, 0) + 1
            ans += dp[j].get(d, 0)
    return ans
print(numberOfArithmeticSlices([2,4,6,8,10]))
print(numberOfArithmeticSlices([7,7,7,7,7]))
