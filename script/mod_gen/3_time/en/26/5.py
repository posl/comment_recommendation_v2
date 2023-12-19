def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def isPossible(maxSum):
        count = 1
        currSum = 0
        for num in nums:
            currSum += num
            if currSum > maxSum:
                currSum = num
                count += 1
                if count > k:
                    return False
        return True
    
    left, right = max(nums), sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if isPossible(mid):
            right = mid
        else:
            left = mid + 1
    return left
print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
