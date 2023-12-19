def numArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    dp = [{} for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0) + 1
            count += dp[j].get(diff, 0)
    return count
nums = [2,4,6,8,10]
print(numArithmeticSlices(nums))
nums = [7,7,7,7,7]
print(numArithmeticSlices(nums))
