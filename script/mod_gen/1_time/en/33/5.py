def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Solution 1
    # Time:  O(n^2)
    # Space: O(n)
    # dp[i][j] = # of arithmetic subsequence slices of nums[:i+1] ending with nums[i] with difference nums[i]-nums[j]
    # dp[i][j] = sum(dp[j][k]) + 1, 0 <= k < j, if nums[i]-nums[j] == nums[j]-nums[k]
    #           1, otherwise
    #           0, if i < j
    # return sum(dp[i][j] for i in range(2, len(nums)) for j in range(i))
    # dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    # result = 0
    # for i in range(2, len(nums)):
    #     for j in range(i):
    #         for k in range(j):
    #             if nums[i]-nums[j] == nums[j]-nums[k]:
    #                 dp[i][j] += dp[j][k] + 1
    #                 result += dp[j][k] + 1
    # return result
    # Solution 2
    # Time:  O(n^2)
    # Space: O(n^2)
    # dp[i][j] = # of arithmetic subsequence slices of nums[:i+1] ending with nums[i] with difference nums[i]-nums[j]
    # dp[i][j] = sum(dp[j][k]) + 1, 0 <= k < j, if nums[i]-nums[j] == nums[j]-nums[k]
    #           1, otherwise
    #           0, if i < j
    # return sum(dp[i][j] for i in range(2, len(nums)) for j in range(i))
    # dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    # result = 0
    # for i in range(2, len(nums)):
    #     for j in range(i):
    #         for k in range(j):
    #             if nums[i]-nums[j] == nums[j]-nums[k]:
    #                 dp[i][j]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = numberOfArithmeticSlices(nums)
    print(a)