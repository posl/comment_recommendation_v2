class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        n = len(nums)
        nums.insert(0,1)
        nums.append(1)
        dp = [[0] * (n+2) for _ in range(n+2)]
        for i in range(n-1,-1,-1):
            for j in range(i+2,n+2):
                for k in range(i+1,j):
                    total = nums[i] * nums[k] * nums[j]
                    total += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j],total)
        return dp[0][n+1]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.maxCoins(nums))