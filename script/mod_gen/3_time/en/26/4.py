def minmax(nums, k):
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = (left + right) // 2
        if feasible(nums, mid, k):
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == '__main__':
    minmax()