def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def is_valid(nums, k, target):
        count = 1
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum > target:
                count += 1
                cur_sum = nums[i]
            if count > k:
                return False
        return True
    
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if is_valid(nums, k, mid):
            right = mid
        else:
            left = mid + 1
    return left
print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
