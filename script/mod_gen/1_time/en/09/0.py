class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        target, remainder = divmod(sum(nums), 2)
        if remainder or max(nums) > target: return False
        dp = [True] + [False] * target
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] |= dp[i - num]
        return dp[target]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.canPartition(nums))