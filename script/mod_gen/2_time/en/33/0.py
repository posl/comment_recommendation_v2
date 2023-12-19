def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    # dp[i][diff] stores the number of arithmetic subsequences ending at index i with difference diff
    # diff can be negative
    # dp[i][diff] = sum(dp[j][diff]) + 1 where j < i and diff = nums[i] - nums[j]
    # Since diff can be negative, we use a hashmap to store the number of arithmetic subsequences ending at index i with difference diff
    # dp[i][diff] = dp[j][diff] + 1 where j < i and diff = nums[i] - nums[j]
    # ans = sum(dp[i][diff]) where i = 0 to n - 1 and diff ranges from -2^31 to 2^31 - 1
    # We can use a 2D array to store dp[i][diff] where diff ranges from -2^31 to 2^31 - 1
    # But the space complexity would be O(n^2)
    # We can use a hashmap to store dp[i][diff] where diff ranges from -2^31 to 2^31 - 1
    # The space complexity would be O(n^2)
    n = len(nums)
    dp = [{} for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0) + 1
            ans += dp[j].get(diff, 0)
    return ans

if __name__ == '__main__':
    numberOfArithmeticSlices()