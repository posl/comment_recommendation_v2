class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        size = len(nums)
        dp = [1] * size
        for i in range(1, size):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.lengthOfLIS(nums))