class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [1] * len(nums)
        prev = [-1] * len(nums)
        maxLen = 1
        maxIdx = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > maxLen:
                maxLen = dp[i]
                maxIdx = i
        ans = []
        while maxIdx != -1:
            ans.append(nums[maxIdx])
            maxIdx = prev[maxIdx]
        return ans

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.largestDivisibleSubset(nums))