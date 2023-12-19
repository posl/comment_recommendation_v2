def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    total = sum(nums)
    if total%2 == 1:
        return False
    target = total/2
    nums.sort()
    if nums[-1] > target:
        return False
    if nums[-1] == target:
        return True
    return canPartitionHelper(nums[:-1], target-nums[-1])

if __name__ == '__main__':
    canPartition()