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
        
    l, r = max(nums), sum(nums)
    while l < r:
        mid = l + (r-l)//2
        if valid(mid):
            r = mid
        else:
            l = mid + 1
    return l
print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
print(splitArray([1,4,4], 3))
