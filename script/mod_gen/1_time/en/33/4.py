def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # DP
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    # dp[i][d] = dp[j][d] + 1
    # j = i - 1, i - 2, ..., 0
    # d = nums[i] - nums[j]
    # dp[i][d] is the number of arithmetic subsequences
    # with difference d ending at index i
    # dp[i][d] = dp[j][d] + 1
    # j = i - 1, i - 2, ..., 0
    # d = nums[i] - nums[j]
    # dp[i][d] is the number of arithmetic subsequences
    # with difference d ending at index i
    # dp[i][d] = dp[j][d] + 1
    # j = i - 1, i - 2, ..., 0
    # d = nums[i] - nums[j]
    # dp[i][d] is the number of arithmetic subsequences
    # with difference d ending at index i
    # dp[i][d] = dp[j][d] + 1
    # j = i - 1, i - 2, ..., 0
    # d = nums[i] - nums[j]
    # dp[i][d] is the number of arithmetic subsequences
    # with difference d ending at index i
    # dp[i][d] = dp[j][d] + 1
    # j = i - 1, i - 2, ..., 0
    # d = nums[i] - nums[j]
    # dp[i][d] is the number of arithmetic subsequences
    # with difference d ending at index i
    # dp[i][d] = dp[j][d] + 1
    # j = i - 1, i - 2, ..., 0
    # d = nums[i] - nums[j]
    # dp[i][d] is the number of arithmetic subsequences
    # with difference d ending at index i
    # dp[i][d] = dp[j][d] + 1
    # j = i - 1

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = numberOfArithmeticSlices(nums)
    print(a)