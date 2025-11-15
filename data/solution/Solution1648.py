import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10**9 + 7
        
        # Sort the inventory in descending order
        inventory.sort(reverse=True)
        inventory.append(0)  # Add a zero at the end to handle the last group
        
        n = len(inventory)
        total_value = 0
        width = 1
        
        for i in range(n - 1):
            if inventory[i] > inventory[i + 1]:
                # Calculate the number of balls we can sell at the current price range
                can_sell = width * (inventory[i] - inventory[i + 1])
                if orders >= can_sell:
                    # If we can sell all balls at this price range
                    total_value += width * (inventory[i] + inventory[i + 1] + 1) * (inventory[i] - inventory[i + 1]) // 2
                    total_value %= MOD
                    orders -= can_sell
                else:
                    # If we can't sell all balls at this price range
                    full_rows = orders // width
                    remaining = orders % width
                    total_value += width * (inventory[i] + inventory[i] - full_rows + 1) * full_rows // 2
                    total_value += remaining * (inventory[i] - full_rows)
                    total_value %= MOD
                    return total_value
            width += 1
        
        return total_value

def maxProfit(inventory: List[int], orders: int) -> int:
    return Solution().maxProfit(inventory, orders)