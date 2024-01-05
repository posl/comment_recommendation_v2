def splitArray(nums, k):
    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left + right) // 2
        if valid(nums, k, mid):
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    k = int(input())
    a = splitArray(nums, k)
    print(a)