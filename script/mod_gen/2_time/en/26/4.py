def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def is_valid(nums, mid, k):
        cnt = 1
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum > mid:
                cnt += 1
                curr_sum = num
                if cnt > k:
                    return False
        return True
    
    low = max(nums)
    high = sum(nums)
    while low <= high:
        mid = low + (high-low)//2
        if is_valid(nums, mid, k):
            high = mid - 1
        else:
            low = mid + 1
    return low
print(splitArray([7,2,5,10,8], 2)) #18
