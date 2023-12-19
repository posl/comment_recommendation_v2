def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    print(nums)
    sum = 0
    for num in nums:
        sum += num
    print(sum)
    if sum % 2 != 0:
        return False
    else:
        target = sum // 2
        print(target)
        return helper(nums, 0, target)

if __name__ == '__main__':
    canPartition()