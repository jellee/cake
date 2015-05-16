# Max profit module given array of stock prices
# runtime: O(n)

def get_max_profit (stock_prices_yesterday) :
    minPrice = stock_prices_yesterday[0]
    maxProfit = stock_prices_yesterday[1] - minPrice
    for time in range(1, len(stock_prices_yesterday)) :
        tempPrice = stock_prices_yesterday[time]
        tempProfit = tempPrice - minPrice
        if tempProfit > maxProfit : maxProfit = tempProfit
        if tempPrice < minPrice :
            minPrice = tempPrice
    print("Maximum profit for yesterday is " + str(maxProfit))

if __name__ == "__main__":
    import sys
    prices = []
    for arg in sys.argv[1:]:
        prices.append(int(arg))
    get_max_profit(prices)

    # test arrays
    # get_max_profit([30, 305, 692, 925])
    # get_max_profit([40, 30, 20, 10])
    # get_max_profit([10, 9, 20, 30, 8, 7, 9, 40, 50, 2])