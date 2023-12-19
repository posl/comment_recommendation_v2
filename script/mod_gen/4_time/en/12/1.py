def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    n = len(nums)
    dp = [1 for i in range(n)]
    prev = [-1 for i in range(n)]
    max_idx = 0
    for i in range(n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[max_idx] < dp[i]:
            max_idx = i
    res = []
    while max_idx != -1:
        res.append(nums[max_idx])
        max_idx = prev[max_idx]
    return res[::-1]

if __name__ == '__main__':
    largestDivisibleSubset()