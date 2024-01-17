class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        if len(nums) == 3:
            if nums[1] - nums[0] == nums[2] - nums[1]:
                return 1
            else:
                return 0
        count = 0
        for i in range(len(nums)-2):
            for j in range(i+2, len(nums)):
                if nums[j] - nums[j-1] == nums[i+1] - nums[i]:
                    count += 1
                else:
                    break
        return count

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.numberOfArithmeticSlices(nums))