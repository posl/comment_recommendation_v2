class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            sum += i * nums[i]
        max = sum
        for i in range(1, len(nums)):
            sum = sum - len(nums) * nums[len(nums) - i] + sum
            if sum > max:
                max = sum
        return max

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.maxRotateFunction(nums))