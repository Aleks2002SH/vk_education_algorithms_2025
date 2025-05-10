def maxProfit(prices):
    profit = 0

    min_price = prices[0]
    
    for i in range(1,len(prices)):
        profit = max(profit,prices[i]-min_price)
        min_price = min(prices[i],min_price)
    
    return profit