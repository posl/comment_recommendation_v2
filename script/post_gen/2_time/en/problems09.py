Synthesizing 9/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

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

=======
Suggestion 3

def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False for _ in range(target+1)]
    dp[0] = True

    for num in nums:
        for j in range(target, num-1, -1):
            dp[j] = dp[j] or dp[j-num]

    return dp[target]

=======
Suggestion 4

def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if sum(nums) % 2 != 0:
        return False
    target = sum(nums) // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    return dp[target]

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))

=======
Suggestion 5

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

=======
Suggestion 6

def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[target]

=======
Suggestion 7

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

=======
Suggestion 8

def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    #find the sum of the array
    total = sum(nums)
    #if the sum is odd, return false
    if total % 2 != 0:
        return False
    #if the sum is even, find the half of the sum
    half = int(total/2)
    #create a dp array with the size of half + 1
    dp = [False] * (half + 1)
    dp[0] = True
    #loop through the array
    for num in nums:
        #loop through the dp array from half to the number
        for i in range(half, num - 1, -1):
            #if the dp at i - num is true, set the dp at i to true
            if dp[i - num]:
                dp[i] = True
    #return the last element of the dp array
    return dp[-1]

=======
Suggestion 9

def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    return dp[target]
