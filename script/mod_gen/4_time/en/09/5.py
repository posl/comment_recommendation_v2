def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    return dfs(nums, target, 0, {})

if __name__ == '__main__':
    canPartition()