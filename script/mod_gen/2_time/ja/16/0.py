class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        #dp[i] := targetがiのときの組み合わせの数
        #dp[i] = sum(dp[i - num] for num in nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target + 1):
            dp[i] += sum(dp[i - num] for num in nums if i - num >= 0)
        return dp[target]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    target = int(input())
    a = Solution()
    print(a.combinationSum4(nums, target))