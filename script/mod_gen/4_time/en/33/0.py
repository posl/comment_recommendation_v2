from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        dp = [defaultdict(int) for _ in range(n)]
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    res += dp[j][diff]
        return res

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.numberOfArithmeticSlices(nums))