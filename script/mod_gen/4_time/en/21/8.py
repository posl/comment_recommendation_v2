def numberOfArithmeticSlices(nums):
    n = len(nums)
    if n < 3:
        return 0
    dp = [0] * n
    for i in range(2, n):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            dp[i] = dp[i - 1] + 1
    return sum(dp)
print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1]))
print(numberOfArithmeticSlices([1,2,3,8,9,10]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10]))
