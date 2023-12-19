def largestDivisibleSubset(nums):
    nums.sort()
    dp = [1 for _ in range(len(nums))]
    parent = [-1 for _ in range(len(nums))]
    maxIndex = 0
    maxSize = 0
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                parent[i] = j
        if maxSize < dp[i]:
            maxSize = dp[i]
            maxIndex = i
    res = []
    while maxIndex != -1:
        res.append(nums[maxIndex])
        maxIndex = parent[maxIndex]
    return res
print(largestDivisibleSubset([1,2,3]))
print(largestDivisibleSubset([1,2,4,8]))
print(largestDivisibleSubset([2,4,6,8,10]))
print(largestDivisibleSubset([3,4,16,8]))
print(largestDivisibleSubset([1,2,4,8,9,72]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,30,60]))
print(largestDivisibleSubset([1,2,4,8,16,32,64,128,256,512,1024]))
print(largestDivisibleSubset([1,2,4,8,16,32,64,128,256,512,1024,3,9,27,81,243,729]))
print(largestDivisibleSubset([1,2,4,8,16,32,64,128,256,512,1024,3,9,27,81,243,729,5,25,125,625]))
