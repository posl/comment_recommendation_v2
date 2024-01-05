def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    # dp[i][diff] represents the number of arithmetic subsequences with difference diff ending at index i.
    # dp[i][diff] = sum(dp[j][diff]) + 1, where j < i and diff == nums[i] - nums[j]
    # ans = sum(dp[i][diff]) for i in range(1, len(nums))
    # Note: it is also possible to solve this problem in O(n^2) time and O(n) space.
    # dp[i] represents the number of arithmetic subsequences ending at index i.
    # dp[i] = sum(dp[j]) + 1, where j < i and nums[i] - nums[j] == nums[j] - nums[k] and k < j
    # ans = sum(dp[i]) for i in range(1, len(nums))
    dp = [{} for _ in range(len(nums))]
    ans = 0
    for i in range(1, len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            if diff not in dp[i]:
                dp[i][diff] = 0
            if diff not in dp[j]:
                dp[j][diff] = 0
            dp[i][diff] += dp[j][diff] + 1
            ans += dp[j][diff]
    return ans

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = numberOfArithmeticSlices(nums)
    print(a)