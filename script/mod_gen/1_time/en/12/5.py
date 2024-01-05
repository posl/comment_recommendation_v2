def largestDivisibleSubset(nums):
    nums.sort()
    dp = [[num] for num in nums]
    for i in range(0, len(nums)):
        for j in range(0, i):
            if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [nums[i]]
    return max(dp, key=len)

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = largestDivisibleSubset(nums)
    print(a)