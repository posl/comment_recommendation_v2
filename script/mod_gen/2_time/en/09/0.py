def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if sum(nums)%2 != 0:
        return False
    target = sum(nums)//2
    nums.sort(reverse=True)
    if nums[0]>target:
        return False
    if nums[0]==target:
        return True
    return helper(nums, target, 0, 0)

if __name__ == '__main__':
    canPartition()