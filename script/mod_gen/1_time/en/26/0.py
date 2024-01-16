class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        #print(nums, k)
        if len(nums) == 1: return nums[0]
        if k == 1: return sum(nums)
        if k == len(nums): return max(nums)
        if k == 2:
            return max(sum(nums[:i]) for i in range(1, len(nums)))
        else:
            for i in range(1, len(nums)):
                if self.splitArray(nums[i:], k - 1) < self.splitArray(nums[i:], k):
                    return self.splitArray(nums[i:], k - 1)
            return self.splitArray(nums, k - 1)

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    k = int(input())
    a = Solution()
    print(a.splitArray(nums, k))