class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        # dp[i][j] := nums[:i]をj個の部分列に分割したときの最小の部分列の最大値
        dp = [[float("inf")] * (k + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = 0
        # 累積和を計算
        acc = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            acc[i + 1] = acc[i] + num
        for i in range(1, len(nums) + 1):
            for j in range(1, k + 1):
                for l in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[l][j - 1], acc[i] - acc[l]))
        return dp[-1][-1]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    k = int(input())
    a = Solution()
    print(a.splitArray(nums, k))