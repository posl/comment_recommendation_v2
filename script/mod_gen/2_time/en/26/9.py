def splitArray(nums, k):
    def valid(mid):
        total, cnt = 0, 1
        for num in nums:
            total += num
            if total > mid:
                total = num
                cnt += 1
                if cnt > k:
                    return False
        return True
    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left + right) // 2
        if valid(mid):
            right = mid
        else:
            left = mid + 1
    return left
nums = [7,2,5,10,8]
k = 2
print(splitArray(nums, k))
nums = [1,2,3,4,5]
k = 2
print(splitArray(nums, k))
nums = [1,4,4]
k = 3
print(splitArray(nums, k))
