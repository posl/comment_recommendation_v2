def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    dp = [{} for i in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0) + 1
            res += dp[j].get(diff, 0)
    return res

if __name__ == '__main__':
    numberOfArithmeticSlices()