def largestDivisibleSubset(nums):
    nums.sort()
    n = len(nums)
    dp = [1]*n
    parent = [-1]*n
    max_ind = 0
    max_val = 0
    for i in range(n):
        for j in range(i):
            if nums[i]%nums[j]==0 and dp[i]<dp[j]+1:
                dp[i] = dp[j]+1
                parent[i] = j
        if dp[i]>max_val:
            max_val = dp[i]
            max_ind = i
    res = []
    while max_ind!=-1:
        res.append(nums[max_ind])
        max_ind = parent[max_ind]
    return res
nums = [1,2,3]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8]
print(largestDivisibleSubset(nums))
nums = [2,3,8,9,27]
print(largestDivisibleSubset(nums))
nums = [5,9,18,54,108,540,90,180,360,720]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8,9,72]
print(largestDivisibleSubset(nums))
nums = [4,8,10,240]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8,9,72]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8,9,72]
print(largestDivisibleSubset(nums))
nums = [1,2,3]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8,9,72]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8,9,72]
print(largestDivisibleSubset(nums))
nums = [1,2,3]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8,9,72]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8,9,72]
print(largestDivisibleSubset(nums))
nums = [1,2,3]
print(largestDivisible

if __name__ == '__main__':
    largestDivisibleSubset()