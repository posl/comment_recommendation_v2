def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    n = len(nums)
    if n == 1:
        return nums
    dp = [[0,[]] for i in range(n)]
    for i in range(n):
        dp[i][0] = 1
        dp[i][1].append(nums[i])
    for i in range(1,n):
        for j in range(i):
            if nums[i]%nums[j] == 0:
                if dp[i][0] < dp[j][0]+1:
                    dp[i][0] = dp[j][0]+1
                    dp[i][1] = dp[j][1][:]
                    dp[i][1].append(nums[i])
    max_len = 0
    max_index = 0
    for i in range(n):
        if dp[i][0] > max_len:
            max_len = dp[i][0]
            max_index = i
    return dp[max_index][1]

if __name__ == '__main__':
    largestDivisibleSubset()