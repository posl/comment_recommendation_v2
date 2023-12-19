def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    dp = [defaultdict(int) for _ in range(n)]
    res = 0
    for i in range(1, n):
        for j in range(i):
            d = nums[i] - nums[j]
            dp[i][d] += 1
            if d in dp[j]:
                dp[i][d] += dp[j][d]
                res += dp[j][d]
    return res

if __name__ == '__main__':
    numberOfArithmeticSlices()