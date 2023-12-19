def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    n = len(nums)
    dp = [0 for i in range(n)]
    prev = [-1 for i in range(n)]
    m = 0
    mi = -1
    for i in range(n):
        dp[i] = 1
        for j in range(i-1, -1, -1):
            if nums[i] % nums[j] == 0:
                if 1 + dp[j] > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        if dp[i] >= m:
            m = dp[i]
            mi = i
    ans = []
    while mi != -1:
        ans.append(nums[mi])
        mi = prev[mi]
    return ans
nums = [1,2,3]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8]
print(largestDivisibleSubset(nums))
