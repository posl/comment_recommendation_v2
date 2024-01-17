class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        total = 0
        for i in range(1, len(nums)-1):
            if nums[i-1] - nums[i] == nums[i] - nums[i+1]:
                total += 1
        return total

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.numberOfArithmeticSlices(nums))