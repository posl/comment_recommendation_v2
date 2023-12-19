def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def isValid(nums, mid, k):
        count = 1
        currSum = 0
        for num in nums:
            currSum += num
            if currSum > mid:
                count += 1
                currSum = num
        return count <= k
    
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = (left + right) // 2
        if isValid(nums, mid, k):
            right = mid
        else:
            left = mid + 1
    return left
print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
print(splitArray([1,4,4], 3))
