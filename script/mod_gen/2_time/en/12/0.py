def largestDivisibleSubset(nums):
    if len(nums) == 1:
        return nums
    nums.sort()
    dp = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
    return max(dp, key=len)

if __name__ == '__main__':
    largestDivisibleSubset()