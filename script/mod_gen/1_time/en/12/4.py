def largestDivisibleSubset(nums):
    if len(nums) == 1:
        return nums
    nums.sort()
    dp = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [nums[i]]
    return max(dp, key=len)
print(largestDivisibleSubset([1,2,3]))
print(largestDivisibleSubset([1,2,4,8]))
print(largestDivisibleSubset([1]))
print(largestDivisibleSubset([1,2]))
print(largestDivisibleSubset([3,4,16,8]))
print(largestDivisibleSubset([1,2,4,8,9,72]))
print(largestDivisibleSubset([1,2,4,8,9,72,16,32,64]))
print(largestDivisibleSubset([1,2,4,8,9,72,16,32,64,81,128,256,512,1024]))
print(largestDivisibleSubset([1,2,4,8,9,72,16,32,64,81,128,256,512,1024,2048,4096,8192,16384,32768,65536]))
