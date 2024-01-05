def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    #DP, O(n) time, O(n) space
    #dp[i] = max(dp[i-1], prices[i]-prices[j]+dp[j-2]) for j in range(i)
    #dp[i] = max(dp[i-1], prices[i]-min(prices[:i]))
    #dp[0] = 0
    #dp[1] = max(0, prices[1]-prices[0])
    #dp[2] = max(dp[1], prices[2]-min(prices[:2]))
    #dp[3] = max(dp[2], prices[3]-min(prices[:3]))
    #dp[4] = max(dp[3], prices[4]-min(prices[:4]))
    #dp[5] = max(dp[4], prices[5]-min(prices[:5]))
    #dp[6] = max(dp[5], prices[6]-min(prices[:6]))
    #dp[7] = max(dp[6], prices[7]-min(prices[:7]))
    #dp[8] = max(dp[7], prices[8]-min(prices[:8]))
    #dp[9] = max(dp[8], prices[9]-min(prices[:9]))
    #dp[10] = max(dp[9], prices[10]-min(prices[:10]))
    #dp[11] = max(dp[10], prices[11]-min(prices[:11]))
    #dp[12] = max(dp[11], prices[12]-min(prices[:12]))
    #dp[13] = max(dp[12], prices[13]-min(prices[:13]))
    #dp[14] = max(dp[13], prices[14]-min(prices[:14]))
    #dp[15] = max(dp[14], prices[15]-min(prices[:15]))
    #dp[16] = max(dp[15], prices[16]-min(prices[:16]))
    #dp[17] = max(dp[16], prices[17]-min(prices[:17]))
    #dp[18] = max(dp[17], prices[18]-min(prices[:18]))
    #dp[19] = max(dp[

if __name__ == '__main__':
    prices = list(map(int, input().split()))
    a = maxProfit(prices)
    print(a)