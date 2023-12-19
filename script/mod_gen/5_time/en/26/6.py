def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def check(mid):
        cuts = 0
        cur_sum = 0
        for num in nums:
            cur_sum += num
            if cur_sum > mid:
                cuts += 1
                cur_sum = num
        return cuts + 1 <= k
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left
print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
