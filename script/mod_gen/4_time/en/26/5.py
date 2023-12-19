def splitArray(nums, k):
    
    def isPossible(mid):
        count = 1
        subarraySum = 0
        for num in nums:
            subarraySum += num
            if subarraySum > mid:
                count += 1
                subarraySum = num
        return count <= k
    
    left, right = max(nums), sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if isPossible(mid):
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
