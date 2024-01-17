class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        diff = 0
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                diff += 1
                count += diff
            else:
                diff = 0
        return count

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.numberOfArithmeticSlices(nums))