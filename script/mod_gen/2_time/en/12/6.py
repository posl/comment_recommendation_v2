def largestDivisibleSubset(nums):
    nums.sort()
    dp = [1] * len(nums)
    prev = [-1] * len(nums)
    max_dp = 0
    max_index = -1
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        if max_dp < dp[i]:
            max_dp = dp[i]
            max_index = i
    result = []
    while max_index != -1:
        result.append(nums[max_index])
        max_index = prev[max_index]
    return result[::-1]
nums = [3,4,16,8]
print(largestDivisibleSubset(nums))
