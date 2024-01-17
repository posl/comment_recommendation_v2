class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        result = 0
        for i in range(len(nums) - 2):
            j = i + 1
            diff = nums[j] - nums[i]
            while j < len(nums) - 1 and nums[j + 1] - nums[j] == diff:
                j += 1
            if j - i + 1 >= 3:
                result += ((j - i) * (j - i + 1)) // 2
                i = j
        return result

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.numberOfArithmeticSlices(nums))