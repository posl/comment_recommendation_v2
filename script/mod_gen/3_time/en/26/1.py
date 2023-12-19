def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    # O(N log N)
    # binary search for the minimum largest sum
    # initialize the bounds
    left = max(nums)
    right = sum(nums)
    
    # binary search
    while left < right:
        mid = left + (right - left) // 2
        
        # greedy split
        pieces = 1
        curr_sum = 0
        for num in nums:
            if curr_sum + num > mid:
                pieces += 1
                curr_sum = num
            else:
                curr_sum += num
        
        if pieces > m:
            left = mid + 1
        else:
            right = mid
    
    return left

if __name__ == '__main__':
    splitArray()