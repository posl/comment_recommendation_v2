class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        ans = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                ans += 1
        return ans

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.numberOfArithmeticSlices(nums))