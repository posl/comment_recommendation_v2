def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def valid(mid):
        count = 1
        total = 0
        for num in nums:
            total += num
            if total > mid:
                total = num
                count += 1
                if count > k:
                    return False
        return True
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if valid(mid):
            right = mid
        else:
            left = mid + 1
    return left
print(splitArray([7,2,5,10,8], 2))
