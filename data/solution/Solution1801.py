import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy_backlog = []  # Max-heap for buy orders (use negative prices for max-heap behavior)
        sell_backlog = []  # Min-heap for sell orders
        
        for price, amount, order_type in orders:
            if order_type == 0:  # Buy order
                while amount > 0 and sell_backlog and sell_backlog[0][0] <= price:
                    sell_price, sell_amount = heapq.heappop(sell_backlog)
                    if sell_amount > amount:
                        heapq.heappush(sell_backlog, (sell_price, sell_amount - amount))
                        amount = 0
                    elif sell_amount < amount:
                        amount -= sell_amount
                    else:  # sell_amount == amount
                        amount = 0
                if amount > 0:
                    heapq.heappush(buy_backlog, (-price, amount))
            else:  # Sell order
                while amount > 0 and buy_backlog and -buy_backlog[0][0] >= price:
                    buy_price, buy_amount = heapq.heappop(buy_backlog)
                    if buy_amount > amount:
                        heapq.heappush(buy_backlog, (buy_price, buy_amount - amount))
                        amount = 0
                    elif buy_amount < amount:
                        amount -= buy_amount
                    else:  # buy_amount == amount
                        amount = 0
                if amount > 0:
                    heapq.heappush(sell_backlog, (price, amount))
        
        total_orders = sum(amount for _, amount in buy_backlog) + sum(amount for _, amount in sell_backlog)
        return total_orders % (10**9 + 7)

def getNumberOfBacklogOrders(orders: List[List[int]]) -> int:
    return Solution().getNumberOfBacklogOrders(orders)