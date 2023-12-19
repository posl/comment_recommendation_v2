def largestDivisibleSubset(nums):
    nums.sort()
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n
    max_idx = 0
    for i in range(n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[max_idx] < dp[i]:
            max_idx = i
    ans = []
    while max_idx != -1:
        ans.append(nums[max_idx])
        max_idx = prev[max_idx]
    return ans[::-1]

if __name__ == '__main__':
    largestDivisibleSubset()