class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum = 0
        for i in nums:
            sum += i
        if sum % 2 != 0:
            return False
        sum = sum // 2
        dp = [False] * (sum + 1)
        dp[0] = True
        for i in nums:
            for j in range(sum, 0, -1):
                if j >= i:
                    dp[j] |= dp[j - i]
        return dp[sum]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.canPartition(nums))