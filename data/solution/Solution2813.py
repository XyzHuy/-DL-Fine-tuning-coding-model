import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        # Sort items by profit in descending order
        items.sort(reverse=True, key=lambda x: x[0])
        
        # Set to keep track of distinct categories
        distinct_categories = set()
        # List to keep track of the profits of items with duplicate categories
        duplicate_profits = []
        
        total_profit = 0
        max_elegance = 0
        
        # Select the first k items
        for i in range(k):
            profit, category = items[i]
            total_profit += profit
            if category in distinct_categories:
                duplicate_profits.append(profit)
            else:
                distinct_categories.add(category)
            
            # Calculate the elegance
            elegance = total_profit + len(distinct_categories) ** 2
            max_elegance = max(max_elegance, elegance)
        
        # Try to replace items with duplicates to get more distinct categories
        for i in range(k, len(items)):
            if not duplicate_profits:
                break
            profit, category = items[i]
            if category not in distinct_categories:
                # Remove the smallest profit from duplicates
                total_profit -= duplicate_profits.pop()
                # Add the new item's profit
                total_profit += profit
                # Add the new category
                distinct_categories.add(category)
                
                # Calculate the elegance
                elegance = total_profit + len(distinct_categories) ** 2
                max_elegance = max(max_elegance, elegance)
        
        return max_elegance

def findMaximumElegance(items: List[List[int]], k: int) -> int:
    return Solution().findMaximumElegance(items, k)