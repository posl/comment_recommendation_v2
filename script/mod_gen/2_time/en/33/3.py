def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    n = len(nums)
    dp = [{} for _ in range(n)]
    ans = 0
    for i in range(1, n):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + 1
            if diff in dp[j]:
                dp[i][diff] += dp[j][diff]
                ans += dp[j][diff]
    return ans

if __name__ == '__main__':
    numberOfArithmeticSlices()