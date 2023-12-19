def splitArray(nums, k):
    def isPossible(m):
        cnt = 0
        curr = 0
        for x in nums:
            if curr + x > m:
                cnt += 1
                curr = x
            else:
                curr += x
        return cnt + 1 <= k
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = (left + right) // 2
        if isPossible(mid):
            right = mid
        else:
            left = mid + 1
    return left
print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
print(splitArray([1,4,4], 3))
print(splitArray([1,4,4], 2))
print(splitArray([1,4,4], 1))
print(splitArray([1,4,4], 4))
print(splitArray([1,2147483647], 2))
