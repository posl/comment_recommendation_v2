def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    dp = [{} for item in nums]
    for i in range(len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0) + 1
            ans += dp[j].get(diff, 0)
    return ans

if __name__ == '__main__':
    numberOfArithmeticSlices()