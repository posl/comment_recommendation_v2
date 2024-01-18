class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        # 動的計画法
        # dp[i] := 長さ i の等差数列の個数
        # dp[i] = dp[i-1] + 1
        # ただし、nums[i-2] - nums[i-1] == nums[i-1] - nums[i] の場合
        # dp[i] = dp[i-1]
        n = len(nums)
        dp = [0] * n
        for i in range(2, n):
            if nums[i-2] - nums[i-1] == nums[i-1] - nums[i]:
                dp[i] = dp[i-1] + 1
        return sum(dp)

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.numberOfArithmeticSlices(nums))