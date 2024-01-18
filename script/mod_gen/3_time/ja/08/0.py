class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        else:
            arr = [0] * n
            for i in range(n):
                arr[i] = sum([nums[j] * j for j in range(n)])
                nums = nums[1:] + nums[:1]
            return max(arr)

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.maxRotateFunction(nums))