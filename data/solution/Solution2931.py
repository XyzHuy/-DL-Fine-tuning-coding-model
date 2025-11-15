import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        # Initialize a min-heap with the rightmost item from each shop
        min_heap = []
        for i, shop in enumerate(values):
            heapq.heappush(min_heap, (shop[-1], i, len(shop) - 1))
        
        total_spent = 0
        day = 1
        
        while min_heap:
            # Pop the smallest value item from the heap
            value, shop_index, item_index = heapq.heappop(min_heap)
            # Add the cost to the total spent
            total_spent += value * day
            day += 1
            
            # If there are more items in the same shop, push the next item to the heap
            if item_index > 0:
                item_index -= 1
                next_value = values[shop_index][item_index]
                heapq.heappush(min_heap, (next_value, shop_index, item_index))
        
        return total_spent

def maxSpending(values: List[List[int]]) -> int:
    return Solution().maxSpending(values)