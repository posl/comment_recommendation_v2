class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        nums.sort()
        return self.search(nums, target)

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.canPartition(nums))