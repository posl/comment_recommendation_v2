from collections import Counter
class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        # Time:  O(n^2)
        # Space: O(n^2)
        ans = 0
        dp = [Counter() for _ in nums]
        for i in range(len(nums)):
            for j in range(i):
                dp[i][nums[i] - nums[j]] += 1
                if nums[i] - nums[j] in dp[j]:
                    dp[i][nums[i] - nums[j]] += dp[j][nums[i] - nums[j]]
                    ans += dp[j][nums[i] - nums[j]]
        return ans

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.numberOfArithmeticSlices(nums))