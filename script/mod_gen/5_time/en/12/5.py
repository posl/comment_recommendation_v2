def largestDivisibleSubset(nums):
    if len(nums) == 1:
        return nums
    nums.sort()
    dp = [1] * len(nums)
    prev = [-1] * len(nums)
    max_ind = 0
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        if dp[max_ind] < dp[i]:
            max_ind = i
    result = []
    while max_ind != -1:
        result.append(nums[max_ind])
        max_ind = prev[max_ind]
    return result[::-1]
print(largestDivisibleSubset([1, 2, 3]))
print(largestDivisibleSubset([1, 2, 4, 8]))
print(largestDivisibleSubset([1, 2, 3, 4, 5, 6, 7, 8]))
print(largestDivisibleSubset([1, 2, 4, 8, 16, 32, 64, 128]))
print(largestDivisibleSubset([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(largestDivisibleSubset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(largestDivisibleSubset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]))
print(largestDivisibleSubset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 200]))
print(largestDivisibleSubset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 200, 300]))
print(largestDivisibleSubset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 200, 300, 400]))
print(l

if __name__ == '__main__':
    largestDivisibleSubset()