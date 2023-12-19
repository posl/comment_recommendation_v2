def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def check(mid):
        cuts = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum > mid:
                cuts += 1
                curr_sum = num
        return cuts + 1
    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left + right) // 2
        if check(mid) <= k:
            right = mid
        else:
            left = mid + 1
    return left
print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
