def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    
    def check(mid):
        total = 0
        count = 1
        for num in nums:
            total += num
            if total > mid:
                total = num
                count += 1
                if count > m:
                    return False
        return True
    
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == '__main__':
    splitArray()