def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    dp = [{} for _ in range(len(nums))]
    ans = 0
    for i in range(1,len(nums)):
        for j in range(i):
            delta = nums[i] - nums[j]
            if delta in dp[j]:
                dp[i][delta] = dp[j][delta] + 1
                ans += dp[j][delta]
            else:
                dp[i][delta] = 1
    return ans

if __name__ == '__main__':
    numberOfArithmeticSlices()