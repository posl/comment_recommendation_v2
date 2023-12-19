def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if len(nums) <= 1:
        return nums
    nums.sort()
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    max_index = dp.index(max(dp))
    res = [nums[max_index]]
    for i in range(max_index - 1, -1, -1):
        if res[-1] % nums[i] == 0 and dp[i] == dp[max_index] - 1:
            res.append(nums[i])
            max_index = i
    return res[::-1]

if __name__ == '__main__':
    largestDivisibleSubset()