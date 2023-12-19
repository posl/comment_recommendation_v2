def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # O(n^2) solution
    # dp[i] = length of longest increasing subsequence ending at index i
    # dp[i] = max(dp[j] + 1 for j in range(i) if nums[j] < nums[i])
    # return max(dp)
    
    # O(n log n) solution
    # tails[i] = smallest tail of all increasing subsequences of length i+1
    # tails[i] = min(tails[j] for j in range(i) if tails[j] >= nums[i])
    # return len(tails)
    
    tails = []
    for num in nums:
        i = bisect.bisect_left(tails, num)
        if i == len(tails):
            tails.append(num)
        else:
            tails[i] = num
    return len(tails)

if __name__ == '__main__':
    lengthOfLIS()