class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        for i in range(0, len(nums)-2):
            diff = nums[i+1] - nums[i]
            for j in range(i+1, len(nums)-1):
                if nums[j+1] - nums[j] == diff:
                    count += 1
                else:
                    break
        return count

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.numberOfArithmeticSlices(nums))