class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums)%2 == 1:
            return False
        nums.sort()
        for i in range(len(nums)):
            if self.dfs(nums, i, sum(nums)//2):
                return True
        return False

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.canPartition(nums))