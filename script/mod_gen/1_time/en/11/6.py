def lengthOfLIS(nums):
    # Time: O(n^2)
    # Space: O(n)
    # dp[i] = length of longest increasing subsequence ending at index i
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = lengthOfLIS(nums)
    print(a)