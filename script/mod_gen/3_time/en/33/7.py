def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    total = 0
    dp = [{} for item in nums]
    for i in range(len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + 1
            if diff in dp[j]:
                dp[i][diff] += dp[j][diff]
                total += dp[j][diff]
    return total

if __name__ == '__main__':
    numberOfArithmeticSlices()