def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    #if prices is empty return 0
    if not prices:
        return 0
    #create a list of length prices and initialize it to 0
    profits = [0] * len(prices)
    #loop through prices
    for i in range(1, len(prices)):
        #loop through prices from 0 to i
        for j in range(i):
            #if prices[i] - prices[j] is greater than profits[i]
            if prices[i] - prices[j] > profits[i]:
                #set profits[i] to prices[i] - prices[j]
                profits[i] = prices[i] - prices[j]
                #if j is greater than 2
                if j > 2:
                    #set profits[i] to profits[j-2] + prices[i] - prices[j]
                    profits[i] = profits[j-2] + prices[i] - prices[j]
                #if profits[i] is greater than profits[i-1]
                if profits[i] > profits[i-1]:
                    #set profits[i] to profits[i-1]
                    profits[i] = profits[i-1]
    #return profits[-1]
    return profits[-1]

if __name__ == '__main__':
    maxProfit()