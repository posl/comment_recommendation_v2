def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    dp = [{} for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i):
            d = nums[i] - nums[j]
            c1 = dp[j].get(d, 0)
            c2 = dp[i].get(d, 0)
            ans += c1
            dp[i][d] = c1 + c2 + 1
    return ans

if __name__ == '__main__':
    numberOfArithmeticSlices()