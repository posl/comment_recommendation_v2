class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        if len(nums) == 1: return 0
        max = 0
        for i in range(len(nums)):
            max += i * nums[i]
        for i in range(1,len(nums)):
            temp = 0
            for j in range(len(nums)):
                temp += j * nums[(i+j)%len(nums)]
            if temp > max:
                max = temp
        return max

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.maxRotateFunction(nums))