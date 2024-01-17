class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        ma

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.maxRotateFunction(nums))