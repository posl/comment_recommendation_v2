def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Solution 1:
    # Time Complexity: O(N^3)
    # Space Complexity: O(1)
    # if len(nums) < 3:
    #     return 0
    # res = 0
    # for i in range(len(nums) - 2):
    #     for j in range(i + 1, len(nums) - 1):
    #         diff = nums[j] - nums[i]
    #         for k in range(j + 1, len(nums)):
    #             if nums[k] - nums[j] == diff:
    #                 res += 1
    # return res
    # Solution 2:
    # Time Complexity: O(N^2)
    # Space Complexity: O(N^2)
    # if len(nums) < 3:
    #     return 0
    # res = 0
    # dp = [{} for _ in range(len(nums))]
    # for i in range(1, len(nums)):
    #     for j in range(i):
    #         diff = nums[i] - nums[j]
    #         if diff in dp[j]:
    #             dp[i][diff] = dp[j][diff] + 1
    #             res += dp[j][diff]
    #         else:
    #             dp[i][diff] = 1
    # return res
    # Solution 3:
    # Time Complexity: O(N^2)
    # Space Complexity: O(N^2)
    if len(nums) < 3:
        return 0
    res = 0
    dp = [{} for _ in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            if diff in dp[j]:
                dp[i][diff] = dp[j][diff] + 1
                res += dp[j][diff]
            else:
                dp[i][diff] = 1
    return res

if __name__ == '__main__':
    numberOfArithmeticSlices()