class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        s = sum(nums)
        ans = sum([i * nums[i] for i in range(n)])
        for i in range(n - 1):
            ans += s - nums[n - 1 - i] * n
            if ans > s:
                s = ans
        return ans

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.maxRotateFunction(nums))