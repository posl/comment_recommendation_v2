class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.largestDivisibleSubset(nums))