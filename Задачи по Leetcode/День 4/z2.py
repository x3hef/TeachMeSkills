# Задание 2

prices = [7,1,5,3,6,4]


def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0
    for i in prices:
        if i < min_price:
            min_price = i
        else:
            profit = i - min_price

            if profit > max_profit:
                max_profit = profit

    return max_profit

print(maxProfit(prices))