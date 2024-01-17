class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if self.is_valid(nums, mid, k):
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    k = int(input())
    a = Solution()
    print(a.splitArray(nums, k))