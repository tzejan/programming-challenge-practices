
def getMaxProfit(prices):
    max_profit = 0
    lowest = 9223372036854775807

    for p in prices:
        if p < lowest:
            lowest = p
            continue
        if p - lowest > max_profit:
            max_profit = p - lowest
    return max_profit


prices = [8, 10, 1, 7, 3]
print getMaxProfit(prices)