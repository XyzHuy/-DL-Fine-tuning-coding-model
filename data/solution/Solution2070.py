import random
import functools
import collections
import string
import math
import datetime


from typing import List
from bisect import bisect_right

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items by price
        items.sort()
        
        # Create a list of maximum beauty up to each price
        max_beauty = [0] * len(items)
        max_beauty[0] = items[0][1]
        for i in range(1, len(items)):
            max_beauty[i] = max(max_beauty[i - 1], items[i][1])
        
        # Extract the sorted prices for binary search
        prices = [item[0] for item in items]
        
        # Process each query
        result = []
        for query in queries:
            # Find the rightmost item with price <= query
            idx = bisect_right(prices, query)
            if idx > 0:
                result.append(max_beauty[idx - 1])
            else:
                result.append(0)
        
        return result

def maximumBeauty(items: List[List[int]], queries: List[int]) -> List[int]:
    return Solution().maximumBeauty(items, queries)