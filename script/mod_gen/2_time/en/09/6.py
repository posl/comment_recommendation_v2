def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    total = sum(nums)
    if total%2!=0:
        return False
    else:
        return canPartitionHelper(nums, total/2, 0)

if __name__ == '__main__':
    canPartition()