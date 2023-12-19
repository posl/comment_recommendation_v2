def numberOfArithmeticSlices(nums):
    n = len(nums)
    dp = [defaultdict(int) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i):
            d = nums[i] - nums[j]
            cnt = dp[j][d]
            ans += cnt
            dp[i][d] += cnt + 1
    return ans

if __name__ == '__main__':
    numberOfArithmeticSlices()