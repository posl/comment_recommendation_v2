def maxCoins(nums):
    def dfs(nums, cache, left, right):
        if left + 1 == right:
            return 0
        if cache[left][right] > 0:
            return cache[left][right]
        result = 0
        for i in range(left + 1, right):
            result = max(result, nums[left] * nums[i] * nums[right] + dfs(nums, cache, left, i) + dfs(nums, cache, i, right))
        cache[left][right] = result
        return result
    nums = [1] + nums + [1]
    cache = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    return dfs(nums, cache, 0, len(nums) - 1)
print(maxCoins([3,1,5,8]))
print(maxCoins([1,5]))
