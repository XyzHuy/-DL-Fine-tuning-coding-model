import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxPrice(self, items: List[List[int]], capacity: int) -> float:
        # Sort items by price per unit weight in descending order
        items.sort(key=lambda x: x[0] / x[1], reverse=True)
        
        total_price = 0.0
        
        for price, weight in items:
            if capacity == 0:
                break
            if weight <= capacity:
                total_price += price
                capacity -= weight
            else:
                # Take the fraction of the item that fits
                fraction = capacity / weight
                total_price += price * fraction
                capacity = 0
        
        # If we couldn't fill the bag, return -1
        if capacity > 0:
            return -1.0
        
        return total_price

def maxPrice(items: List[List[int]], capacity: int) -> float:
    return Solution().maxPrice(items, capacity)