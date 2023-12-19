def splitArray(nums, k):
    start = max(nums)
    end = sum(nums)
    while start < end:
        mid = (start + end) // 2
        if check(nums, mid, k):
            end = mid
        else:
            start = mid + 1
    return start

if __name__ == '__main__':
    splitArray()