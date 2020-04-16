#!/usr/bin/python

import argparse

# PLAN
# store 3 values:
# FIRST:
# the price to hold (starting at index 0)
# SECOND:
# the price that will be compared to price 1 to see if it's going to yield a profit
# THIRD:
# the profit, initialized to 0

# loop through array first time looking at first price
# loop through again looking at subsequent prices to see the maximum profit
# once maximum profit is found, set that number to profit


def find_max_profit(prices):
    profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] <= prices[i]:
                j += 1
            else:
                profit = prices[j] - prices[i]
                i += 1
                j += 1
        return profit

# def find_max_profit(prices):
#   min_price = prices[0]
#   max_profit = prices[1] - min_price
#   for i in range(1, len(prices)):
#     price = prices[i]
#     max_profit = max(price - min_price, max_profit)
#     min_price = min(price, min_price)
#   return max_profit

prices = [1050, 270, 1540, 3800, 2]

print(find_max_profit(prices))

# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))
