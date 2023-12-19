def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False for _ in range(target + 1)]
    dp[0] = True
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[target]
print(canPartition([1,5,11,5])) # True
print(canPartition([1,2,3,5])) # False
print(canPartition([1,2,3,4,5,6,7])) # True
print(canPartition([1,2,3,4,5,6,8])) # False
print(canPartition([1,2,3,4,5,6,9])) # False
print(canPartition([1,2,3,4,5,6,10])) # True
print(canPartition([1,2,3,4,5,6,11])) # False
print(canPartition([1,2,3,4,5,6,12])) # True
print(canPartition([1,2,3,4,5,6,13])) # False
print(canPartition([1,2,3,4,5,6,14])) # True
print(canPartition([1,2,3,4,5,6,15])) # False
print(canPartition([1,2,3,4,5,6,16])) # True
print(canPartition([1,2,3,4,5,6,17])) # False
print(canPartition([1,2,3,4,5,6,18])) # True
print(canPartition([1,2,3,4,5,6,19])) # False
print(canPartition([1,2,3,4,5,6,20])) # True
print(canPartition([1,2,3,4,5,6,21])) # False
print(canPartition([1,2,3,4,5,6,22])) # True
print(canPartition([1,2,3,4,5,6,23])) # False
print

if __name__ == '__main__':
    canPartition()