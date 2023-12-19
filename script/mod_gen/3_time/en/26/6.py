def split_array(nums,k):
    def split_array_helper(nums, k, start, end, memo):
        if (start, end, k) in memo:
            return memo[(start, end, k)]
        if k == 1:
            return sum(nums[start:end+1])
        if start == end:
            return nums[start]
        min_split = float("inf")
        for i in range(start, end):
            min_split = min(min_split, max(split_array_helper(nums, k-1, start, i, memo), sum(nums[i+1:end+1])))
        memo[(start, end, k)] = min_split
        return min_split
    return split_array_helper(nums, k, 0, len(nums)-1, {})
print(split_array([7,2,5,10,8], 2))
print(split_array([1,2,3,4,5], 2))
print(split_array([1,4,4], 3))
