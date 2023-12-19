def largestDivisibleSubset(nums):
    if len(nums) == 0:
        return []
    nums.sort()
    dp = [1 for _ in range(len(nums))]
    prev = [-1 for _ in range(len(nums))]
    max_index = 0
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        if dp[max_index] < dp[i]:
            max_index = i
    res = []
    while max_index != -1:
        res.append(nums[max_index])
        max_index = prev[max_index]
    return res[::-1]
print(largestDivisibleSubset([1,2,3]))
print(largestDivisibleSubset([1,2,4,8]))
print(largestDivisibleSubset([1,2,4,8,9,72]))
