def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def isPossible(nums, k, mid):
        current_sum = 0
        splits = 1
        for num in nums:
            current_sum += num
            if current_sum > mid:
                splits += 1
                current_sum = num
                if splits > k:
                    return False
        return True
    
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if isPossible(nums, k, mid):
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == '__main__':
    splitArray()