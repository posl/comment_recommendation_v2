def splitArray(nums, k):
    def isPossible(mid, k):
        cnt = 1
        currSum = 0
        for i in nums:
            currSum += i
            if currSum > mid:
                currSum = i
                cnt += 1
                if cnt > k:
                    return False
        return True
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = (left + right) // 2
        if isPossible(mid, k):
            right = mid
        else:
            left = mid + 1
    return left
print(splitArray([7,2,5,10,8],2))
print(splitArray([1,2,3,4,5],2))
print(splitArray([1,4,4],3))
print(splitArray([1,2,3,4,5],1))
