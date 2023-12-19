def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # The idea is to find the sum of the array. If it is odd, then we cannot divide the array into two subsets with equal sum, so we return False. If it is even, then we sort the array in descending order and check if we can find a subset with sum = sum/2
    nums.sort(reverse=True)
    total = sum(nums)
    if total % 2 != 0:
        return False
    else:
        target = total / 2
        return findSubset(nums, target, 0, 0)

if __name__ == '__main__':
    canPartition()