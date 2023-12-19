def splitArray(nums, k):
    def canSplit(nums, k, x):
        count = 0
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            if curr > x:
                curr = nums[i]
                count += 1
                if count >= k:
                    return False
        return True
    
    l, r = max(nums), sum(nums)
    while l < r:
        mid = l + (r - l) // 2
        if canSplit(nums, k, mid):
            r = mid
        else:
            l = mid + 1
    return l
print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
