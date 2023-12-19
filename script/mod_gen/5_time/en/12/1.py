def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    dp = [1] * len(nums)
    prev = [-1] * len(nums)
    max_ind = 0
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] % nums[j] == 0:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        if dp[i] > dp[max_ind]:
            max_ind = i
    ans = []
    while max_ind != -1:
        ans.append(nums[max_ind])
        max_ind = prev[max_ind]
    return ans

if __name__ == '__main__':
    largestDivisibleSubset()