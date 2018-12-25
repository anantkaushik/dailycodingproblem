"""
Given a array of numbers representing the stock prices of a company in chronological order, 
write a function that calculates the maximum profit you could have made from buying and selling that stock once. 
You must buy before you can sell it.
For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and 
sell it at 10 dollars.
"""
def maxProfit(prices):
    if not prices:return 0
    profit, buy = 0, prices[0]
    for price in prices:
        if price > buy:
            profit = (price-buy) if (price-buy) > profit else profit
        else:
            buy = price
    return profit