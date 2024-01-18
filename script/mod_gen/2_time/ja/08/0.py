class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        max = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(len(nums)):
                sum += (j * nums[(i + j) % len(nums)])
            if max < sum:
                max = sum
        return max

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.maxRotateFunction(nums))