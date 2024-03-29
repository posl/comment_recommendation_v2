class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        ans = 0
        for i in range(len(nums)-2):
            diff = nums[i+1] - nums[i]
            for j in range(i+2, len(nums)):
                if nums[j] - nums[j-1] == diff:
                    ans += 1
                else:
                    break
        return ans

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.numberOfArithmeticSlices(nums))