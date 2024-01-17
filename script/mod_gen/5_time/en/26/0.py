class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        while l < r:
            mid = l + (r - l) // 2
            if self.valid(mid, nums, k):
                r = mid
            else:
                l = mid + 1
        return l

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    k = int(input())
    a = Solution()
    print(a.splitArray(nums, k))