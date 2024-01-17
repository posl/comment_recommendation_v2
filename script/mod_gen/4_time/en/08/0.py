class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        max_sum = -999999
        for i in range(n):
            sum = 0
            for j in range(n):
                sum += j * nums[j]
            if sum > max_sum:
                max_sum = sum
            nums.insert(0, nums.pop())
        return max_sum

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.maxRotateFunction(nums))