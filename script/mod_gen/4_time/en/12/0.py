class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) >= len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.largestDivisibleSubset(nums))