def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def is_valid(nums, k, mid):
        count = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum > mid:
                count += 1
                curr_sum = num
                if count >= k:
                    return False
        return True
    
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = (left + right) // 2
        if is_valid(nums, k, mid):
            right = mid
        else:
            left = mid + 1
    return left
    
print(splitArray([7,2,5,10,8], 2))
