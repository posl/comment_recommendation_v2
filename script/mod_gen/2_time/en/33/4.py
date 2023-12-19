def numberOfArithmeticSlices(nums):
    n = len(nums)
    dp = [dict() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i):
            d = nums[i] - nums[j]
            sum = dp[j].get(d, 0)
            origin = dp[i].get(d, 0)
            dp[i][d] = origin + sum + 1
            ans += sum
    return ans
nums = [2,4,6,8,10]
print(numberOfArithmeticSlices(nums))
nums = [7,7,7,7,7]
print(numberOfArithmeticSlices(nums))
