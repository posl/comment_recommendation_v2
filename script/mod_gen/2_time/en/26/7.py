def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def is_valid(nums, k, target):
        count = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total > target:
                total = nums[i]
                count += 1
        count += 1
        return count <= k
    
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if is_valid(nums, k, mid):
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
print(splitArray([
