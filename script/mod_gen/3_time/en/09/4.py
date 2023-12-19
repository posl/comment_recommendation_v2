def canPartition(nums):
    if sum(nums)%2 != 0:
        return False
    else:
        return True
print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
