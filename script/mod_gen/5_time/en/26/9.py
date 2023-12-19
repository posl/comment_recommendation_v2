def splitArray(nums, k):
    def check(mid):
        count = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum > mid:
                count += 1
                curr_sum = num
                if count >= k:
                    return False
        return True
    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left + right) // 2
        if check(mid):
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
print(splitArray([1,4,4], 5))
print(splitArray([1,2147483647], 2))
print(splitArray([1,2147483647], 1))
print(splitArray([1,2147483647], 3))
print(splitArray([1,2147483647], 4))
print(splitArray([1,2147483647], 5))
print(splitArray([1,2147483647], 6))
print(splitArray([1,2147483647], 7))
print(splitArray([1,2147483647], 8))
print(splitArray([1,2147483647], 9))
print(splitArray([1,2147483647], 10))
print(splitArray([1,2147483647], 11))
print(splitArray([1,2147483647], 12))
print(splitArray([1,2147483647], 13))
print(splitArray([1,2147483647], 14))
print(splitArray([1,2147483647], 15))
print(splitArray([1,2147483647], 16))
print(splitArray([1,2147483647], 17))
print(splitArray([1,2147483647], 18))
print(splitArray([1,2147483647], 19))
print(splitArray([1,2147483647],
