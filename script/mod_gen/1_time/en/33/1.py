def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #dp[i][d] represents the number of arithmetic subsequences ending with nums[i] and its common difference is d.
    #dp[i][d] += dp[j][d] + 1, where j < i and nums[i] - nums[j] == d.
    #Time: O(n^2)
    #Space: O(n^2)
    dp = [dict() for _ in range(len(nums))]
    res = 0
    for i in range(1, len(nums)):
        for j in range(i):
            d = nums[i] - nums[j]
            dp[i][d] = dp[i].get(d, 0) + dp[j].get(d, 0) + 1
            res += dp[j].get(d, 0)
    return res

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = numberOfArithmeticSlices(nums)
    print(a)