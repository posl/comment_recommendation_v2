class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        dp = [True] + [False] * target
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] |= dp[i - num]
        return dp[-1]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.canPartition(nums))