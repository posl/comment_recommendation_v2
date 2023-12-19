def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    def is_valid(nums, m, max_sum):
        splits, curr_sum = 1, 0
        for n in nums:
            if curr_sum + n > max_sum:
                splits += 1
                curr_sum = n
            else:
                curr_sum += n
        return splits <= m
    
    left, right = max(nums), sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if is_valid(nums, m, mid):
            right = mid
        else:
            left = mid + 1
    return left
nums = [7,2,5,10,8]
k = 2
print(splitArray(nums, k))
nums = [1,2,3,4,5]
k = 2
print(splitArray(nums, k))
