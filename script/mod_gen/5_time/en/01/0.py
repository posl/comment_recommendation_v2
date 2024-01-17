class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    target = int(input())
    a = Solution()
    print(a.twoSum(nums, target))