def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #dp = [collections.defaultdict(int) for _ in nums]
    dp = [{} for _ in nums]
    res = 0
    for i in range(len(nums)):
        for j in range(i):
            dp[i][nums[i] - nums[j]] = dp[i].get(nums[i] - nums[j], 0) + dp[j].get(nums[i] - nums[j], 0) + 1
            res += dp[j].get(nums[i] - nums[j], 0)
    return res

if __name__ == '__main__':
    numberOfArithmeticSlices()