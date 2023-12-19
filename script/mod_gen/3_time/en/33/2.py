def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    dp = [{} for _ in range(len(nums))]
    result = 0
    for i in range(1, len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            if diff in dp[j]:
                dp[i][diff] = dp[j][diff] + 1
                result += dp[j][diff]
            else:
                dp[i][diff] = 1
    return result

if __name__ == '__main__':
    numberOfArithmeticSlices()