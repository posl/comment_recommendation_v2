def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    def dp(i, j):
        if i + 1 == j: return 0
        if (i, j) in memo: return memo[(i, j)]
        memo[(i, j)] = max(nums[i] * nums[k] * nums[j] + dp(i, k) + dp(k, j) for k in range(i + 1, j))
        return memo[(i, j)]
    nums = [1] + nums + [1]
    memo = {}
    return dp(0, len(nums) - 1)
nums = [3,1,5,8]
print(maxCoins(nums))
nums = [1,5]
print(maxCoins(nums))
