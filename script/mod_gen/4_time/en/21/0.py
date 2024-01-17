class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        dp = [0] * n
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1
        return sum(dp)

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.numberOfArithmeticSlices(nums))