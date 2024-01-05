def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    nums.reverse()
    sum_of_nums = sum(nums)
    if sum_of_nums % 2 != 0:
        return False
    half_sum = sum_of_nums // 2
    if half_sum in nums:
        return True
    for i in range(0, len(nums)):
        sum_of_subset = nums[i]
        if sum_of_subset > half_sum:
            continue
        for j in range(i+1, len(nums)):
            sum_of_subset += nums[j]
            if sum_of_subset > half_sum:
                break
            elif sum_of_subset == half_sum:
                return True
    return False
print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
print(canPartition([1,2,3,4,5,6,7]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16, 17]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16, 17, 18]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16, 17, 18, 19]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16, 17, 18, 19, 20]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16, 17, 18, 19, 20, 21]))
print

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = canPartition(nums)
    print(a)