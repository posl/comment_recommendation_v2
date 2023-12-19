def largestDivisibleSubset(nums):
    n = len(nums)
    nums.sort()
    dp = [1] * n
    prev = [-1] * n
    max_val = 0
    max_idx = -1
    for i in range(n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > max_val:
            max_val = dp[i]
            max_idx = i
    ans = []
    while max_idx != -1:
        ans.append(nums[max_idx])
        max_idx = prev[max_idx]
    return ans[::-1]
print(largestDivisibleSubset([1,2,4,8]))
print(largestDivisibleSubset([1,2,3]))
print(largestDivisibleSubset([1,2,4,8,9,72]))
print(largestDivisibleSubset([4,8,10,240]))
print(largestDivisibleSubset([1,2,4,8,9,72,100,128,240]))
print(largestDivisibleSubset([1,2,4,8,9,72,100,128,240,360]))
print(largestDivisibleSubset([1,2,4,8,9,72,100,128,240,360,480]))
print(largestDivisibleSubset([1,2,4,8,9,72,100,128,240,360,480,720]))
print(largestDivisibleSubset([1,2,4,8,9,72,100,128,240,360,480,720,840]))
print(largestDivisibleSubset([1,2,4,8,9,72,100,128,240,360,480,720,840,960]))
print(largestDivisibleSubset([1,2,4,8,9,72,100,128,240,360,480,720,840,960,1080]))
print(largestDivisibleSubset([1,2,4,8,9,72,100,128,240,360,480,720,840,960,1080,1200]))
print(largestDivisibleSubset([1,2,4,8,9,72,100
