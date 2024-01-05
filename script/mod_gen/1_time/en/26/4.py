def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    l = max(nums)
    r = sum(nums)
    while l < r:
        mid = (l + r) // 2
        if check(nums, mid, k):
            r = mid
        else:
            l = mid + 1
    return l

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    k = int(input())
    a = splitArray(nums, k)
    print(a)