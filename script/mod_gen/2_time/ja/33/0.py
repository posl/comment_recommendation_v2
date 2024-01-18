class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count=0
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                if nums[j]-nums[i]==nums[j+1]-nums[j]:
                    count+=1
                else:
                    break
        return count

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.numberOfArithmeticSlices(nums))