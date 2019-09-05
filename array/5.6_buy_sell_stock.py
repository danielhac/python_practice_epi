# This problem is concerned with the problem of optimally buying and selling a stock once.
# The maximum profit that can be made with one buy and one sell is 30 - buy at 260 and sell at 290. 
# Note that 260 is not the lowest price, nor 290 the highest price.

# Write a program that takes an array denoting the daily stock price, 
# and retums the maximum profit that could be made by 
# buying and then selling one share of that stock. 
# There is no need to buy if no profit is possible.


# O(n^2) time: Brute force:
# Checks all elems after cur elem for max profit in a double while loop
def buy_and_sell_stock_once(prices):
    max_profit = 0.0

    i = 0
    while i < len(prices) - 1:
        j = i + 1
        while j < len(prices):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]
            j += 1
        i += 1
    
    print(max_profit)


# O(n^2) time: Checks all elems after cur elem for max profit in a single while loop
# but iterations from cur ith elem to end
def buy_and_sell_stock_once2(prices):
    max_profit = 0.0

    i = 0
    while i < len(prices) - 1:
        if max(prices[i+1:]) - prices[i] > max_profit:
            max_profit = max(prices[i+1:]) - prices[i]
        i += 1
    
    print(max_profit)


# O(n) time
def buy_and_sell_stock_once3(prices):
    max_profit = 0.0
    low = float('inf')

    for price in prices:
        if price < low:
            low = price
        elif price - low > max_profit:
            max_profit = price - low
    
    print(max_profit)


prices = [310,315,275,295,260,270,290,230,255,250] # 30
# prices = [0.2, 0.1] # 0.0

buy_and_sell_stock_once3(prices)