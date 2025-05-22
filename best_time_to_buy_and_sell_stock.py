def buy_and_sell(prices):
    left = 0
    right = 1
    maxProfit = 0
    
    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
        else:
            left = right
        right += 1
        
    return maxProfit

print(buy_and_sell([7,1,5,3,6,4]))