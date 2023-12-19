def minmax(nums, k):
    def is_valid(mid):
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
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = (left + right) // 2
        if is_valid(mid):
            right = mid
        else:
            left = mid + 1
    return left
print(minmax([7,2,5,10,8], 2))
print(minmax([1,2,3,4,5], 2))
print(minmax([1,4,4], 3))
print(minmax([2,3,1,2,4,3], 5))
