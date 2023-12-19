def largestDivisibleSubset(nums):
    nums.sort()
    dp = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i]%nums[j] == 0 and len(dp[i]) < len(dp[j])+1:
                dp[i] = dp[j] + [nums[i]]
    return max(dp, key=len)
print(largestDivisibleSubset([1,2,3]))
print(largestDivisibleSubset([1,2,4,8]))
print(largestDivisibleSubset([1,2,4,8,16,32,64,128,256]))
print(largestDivisibleSubset([1,2,4,8,16,32,64,128,256,512]))
print(largestDivisibleSubset([1,2,4,8,16,32,64,128,256,512,1024]))
print(largestDivisibleSubset([1,2,4,8,16,32,64,128,256,512,1024,2048]))
print(largestDivisibleSubset([1,2,4,8,16,32,64,128,256,512,1024,2048,4096]))
print(largestDivisibleSubset([1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192]))
print(largestDivisibleSubset([1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384]))
print(largestDivisibleSubset([1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768]))
print(largestDivisibleSubset([1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536]))
print(largestDivisibleSubset([1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072]))
print(largestDivisibleSubset([1,2,4,8,16
