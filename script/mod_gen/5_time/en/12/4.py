def largestDivisibleSubset(nums):
    if len(nums) == 1:
        return nums
    nums.sort()
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    max_index = dp.index(max(dp))
    output = [nums[max_index]]
    for i in range(max_index - 1, -1, -1):
        if output[-1] % nums[i] == 0 and dp[i] == dp[max_index] - 1:
            output.append(nums[i])
            max_index = i
    return output[::-1]
print(largestDivisibleSubset([1,2,3]))
print(largestDivisibleSubset([1,2,4,8]))
print(largestDivisibleSubset([5,9,18,54,108,540,90,180,360,720]))
print(largestDivisibleSubset([4,8,10,240]))
print(largestDivisibleSubset([1,2,4,8,9,72]))
print(largestDivisibleSubset([1,2,4,8,9,72,108,540]))
print(largestDivisibleSubset([1,2,4,8,9,72,108,540,5,10,20,40,80,160,320,640]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,240]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,240,480]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,240,480,960]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10,11,12,
