class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    target = int(input())
    a = Solution()
    print(a.combinationSum4(nums, target))