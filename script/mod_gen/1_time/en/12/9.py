def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    n = len(nums)
    dp = [0] * n
    parent = [0] * n
    mx = 0
    mx_index = -1
    for i in range(n):
        for j in range(i-1,-1,-1):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                parent[i] = j
                if dp[i] > mx:
                    mx = dp[i]
                    mx_index = i
    result = []
    for i in range(mx+1):
        result.append(nums[mx_index])
        mx_index = parent[mx_index]
    return result
print(largestDivisibleSubset([1,2,3]))
print(largestDivisibleSubset([1,2,4,8]))
print(largestDivisibleSubset([2,3,8,9,27]))
print(largestDivisibleSubset([4,8,10,240]))
print(largestDivisibleSubset([1,2,4,8,9,72]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,240]))
