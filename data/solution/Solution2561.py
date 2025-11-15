import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # Count the frequency of each fruit in both baskets
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        
        # Combine the counts and check if each fruit can be evenly split between the two baskets
        combined_count = count1 + count2
        for fruit, count in combined_count.items():
            if count % 2 != 0:
                return -1
        
        # Determine the target count for each fruit in each basket
        target_count = {fruit: count // 2 for fruit, count in combined_count.items()}
        
        # Calculate the excess fruits in each basket that need to be swapped
        to_swap = []
        for fruit in set(basket1 + basket2):
            excess_in_b1 = count1[fruit] - target_count[fruit]
            excess_in_b2 = count2[fruit] - target_count[fruit]
            
            # We only need to consider the positive excess from one basket
            # because the negative excess from the other basket will balance it out
            to_swap.extend([fruit] * abs(excess_in_b1))
        
        # Sort the fruits that need to be swapped by cost
        to_swap.sort()
        
        # The minimum cost to swap is either swapping directly or using the cheapest fruit as a中介
        min_cost_fruit = min(combined_count.keys())
        min_cost = 0
        
        # We only need to consider half of the swaps because each swap involves two fruits
        for i in range(len(to_swap) // 2):
            min_cost += min(to_swap[i], min_cost_fruit * 2)
        
        return min_cost

def minCost(basket1: List[int], basket2: List[int]) -> int:
    return Solution().minCost(basket1, basket2)