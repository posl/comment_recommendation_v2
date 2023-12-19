def largestDivisibleSubset(nums):
    nums.sort()
    n = len(nums)
    dp = [1 for i in range(n)]
    prev = [-1 for i in range(n)]
    max_ind = 0
    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[max_ind] < dp[i]:
            max_ind = i
    ans = []
    while max_ind != -1:
        ans.append(nums[max_ind])
        max_ind = prev[max_ind]
    return ans[::-1]
nums = [1,2,3]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8]
print(largestDivisibleSubset(nums))
nums = [4,8,10,240]
print(largestDivisibleSubset(nums))
