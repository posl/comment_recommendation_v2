def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    n = len(nums)
    dp = [dict() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i):
            d = nums[i] - nums[j]
            if d in dp[j]:
                dp[i][d] = dp[j][d] + 1
                ans += dp[j][d]
            else:
                dp[i][d] = 1
    return ans

if __name__ == '__main__':
    numberOfArithmeticSlices()