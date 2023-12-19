def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n < 3:
        return 0
    dp = [{} for _ in range(n)]
    res = 0
    for i in range(1, n):
        for j in range(i):
            diff = nums[i] - nums[j]
            if diff in dp[j]:
                dp[i][diff] = dp[j][diff] + 1
                res += dp[j][diff]
            else:
                dp[i][diff] = 1
    return res

if __name__ == '__main__':
    numberOfArithmeticSlices()