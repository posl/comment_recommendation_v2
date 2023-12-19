def largestDivisibleSubset(nums):
    nums.sort()
    dp = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(dp[i]) <= len(dp[j]):
                dp[i] = dp[j] + [nums[i]]
    return max(dp, key=len) if dp else []

if __name__ == '__main__':
    largestDivisibleSubset()