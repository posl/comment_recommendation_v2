class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        cnt = 0
        for i in range(len(nums)-2):
            for j in range(i+2, len(nums)):
                if nums[i+1]-nums[i] == nums[j]-nums[j-1]:
                    cnt += 1
                else:
                    break
        return cnt

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.numberOfArithmeticSlices(nums))