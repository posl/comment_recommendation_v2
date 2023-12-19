def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    l, r = max(nums), sum(nums)
    while l < r:
        mid = (l + r) // 2
        if valid(mid, nums, k):
            r = mid
        else:
            l = mid + 1
    return l

if __name__ == '__main__':
    splitArray()