import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Find the maximum cost to determine the size of the frequency array
        max_cost = max(costs)
        
        # Create a frequency array to count the occurrences of each cost
        frequency = [0] * (max_cost + 1)
        
        # Populate the frequency array
        for cost in costs:
            frequency[cost] += 1
        
        # Initialize variables to keep track of the number of ice creams bought and the total cost
        total_cost = 0
        ice_cream_count = 0
        
        # Iterate through the frequency array to buy as many ice creams as possible
        for cost in range(1, max_cost + 1):
            if frequency[cost] == 0:
                continue
            
            # Determine how many ice creams of this cost can be bought
            if total_cost + cost * frequency[cost] <= coins:
                total_cost += cost * frequency[cost]
                ice_cream_count += frequency[cost]
            else:
                # Buy as many as possible with the remaining coins
                while frequency[cost] > 0 and total_cost + cost <= coins:
                    total_cost += cost
                    ice_cream_count += 1
                    frequency[cost] -= 1
        
        return ice_cream_count

def maxIceCream(costs: List[int], coins: int) -> int:
    return Solution().maxIceCream(costs, coins)