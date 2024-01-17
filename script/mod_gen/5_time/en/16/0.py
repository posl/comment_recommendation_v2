class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        for i in range(1, target+1):
            for j in nums:
                if i >= j:
                    dp[i] += dp[i-j]
        return dp[target]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    target = int(input())
    a = Solution()
    print(a.combinationSum4(nums, target))