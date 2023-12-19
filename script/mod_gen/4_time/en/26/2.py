def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def check(mid):
        cuts, curr_sum = 1, 0
        for num in nums:
            curr_sum += num
            if curr_sum > mid:
                cuts += 1
                curr_sum = num
        return cuts <= k
    
    left, right = max(nums), sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == '__main__':
    splitArray()