def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    # dp[i][d] = # of subsequences ending at i with difference d
    # dp[i][d] = sum(dp[j][d]) + 1
    # ans = sum(dp[i][d])
    n = len(nums)
    dp = [{} for _ in range(n)]
    ans = 0
    for i in range(1, n):
        for j in range(i):
            d = nums[i] - nums[j]
            dp[i][d] = dp[i].get(d, 0) + dp[j].get(d, 0) + 1
            ans += dp[j].get(d, 0)
    return ans

if __name__ == '__main__':
    numberOfArithmeticSlices()