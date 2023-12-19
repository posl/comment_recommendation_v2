def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations
    #https://www.youtube.com/watch?v=IFNibRVgFBo
    #https://www.youtube.com/watch?v=ASoaQq66foQ
    #https://www.youtube.com/watch?v=IFNibRVgFBo
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    #https://www.youtube.com/watch?v=FLbqgyJ-70I
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0]*n for _ in range(n)]
    #dp[i][j] = max coins in nums[i:j]
    for l in range(2, n): #length of subarray
        for i in range(n-l): #start index
            j = i + l #end index
            for k in range(i+1, j): #burst index
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j])
    return dp[0][n-1]

if __name__ == '__main__':
    maxCoins()