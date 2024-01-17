class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        maxSum = float('-inf')
        for k in range(n):
            sum = 0
            for i in range(n):
                sum += i * nums[(i + k) % n]
            maxSum = max(maxSum, sum)
        return maxSum

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.maxRotateFunction(nums))