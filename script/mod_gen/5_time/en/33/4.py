def numberOfArithmeticSlices(nums):
    n = len(nums)
    dp = [{} for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0) + 1
            ans += dp[j].get(diff, 0)
    return ans
print(numberOfArithmeticSlices([2,4,6,8,10]))
print(numberOfArithmeticSlices([7,7,7,7,7]))
