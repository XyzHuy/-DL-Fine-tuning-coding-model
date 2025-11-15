import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict
from typing import List

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # Dictionary to store the count of each food item per table
        table_orders = defaultdict(lambda: defaultdict(int))
        # Set to store unique food items
        food_items = set()
        
        # Populate the dictionary and set with orders
        for name, table, food in orders:
            table_orders[table][food] += 1
            food_items.add(food)
        
        # Sort the food items alphabetically
        sorted_food_items = sorted(food_items)
        
        # Prepare the header row
        header = ["Table"] + sorted_food_items
        
        # Prepare the data rows
        table_numbers = sorted(table_orders.keys(), key=lambda x: int(x))
        result = [header]
        for table in table_numbers:
            row = [table]
            for food in sorted_food_items:
                row.append(str(table_orders[table][food]))
            result.append(row)
        
        return result

def displayTable(orders: List[List[str]]) -> List[List[str]]:
    return Solution().displayTable(orders)