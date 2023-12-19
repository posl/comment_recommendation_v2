def largestDivisibleSubset(nums):
    nums.sort()
    n = len(nums)
    dp = [1] * n
    parent = [-1] * n
    max_len = 0
    max_index = -1
    for i in range(n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                parent[i] = j
        if dp[i] > max_len:
            max_len = dp[i]
            max_index = i
    res = []
    while max_index != -1:
        res.append(nums[max_index])
        max_index = parent[max_index]
    return res[::-1]
nums = [1,2,3]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8]
print(largestDivisibleSubset(nums))
