def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    ans = 0
    dp = [defaultdict(int) for _ in range(n)]
    for i in range(n):
        for j in range(i):
            delta = nums[i] - nums[j]
            dp[i][delta] += 1
            if delta in dp[j]:
                dp[i][delta] += dp[j][delta]
                ans += dp[j][delta]
    return ans

if __name__ == '__main__':
    numberOfArithmeticSlices()