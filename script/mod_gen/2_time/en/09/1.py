def canPartition(nums):
    nums.sort()
    total = sum(nums)
    if total % 2 == 1:
        return False
    target = total // 2
    if nums[-1] > target:
        return False
    if nums[-1] == target:
        return True
    return canPartitionHelper(nums, target, 0)

if __name__ == '__main__':
    canPartition()