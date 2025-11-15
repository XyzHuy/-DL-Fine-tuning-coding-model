import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict
from typing import List

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        # Create a dictionary to store the sum of weights for each value
        weight_map = defaultdict(int)
        
        # Add weights from items1
        for value, weight in items1:
            weight_map[value] += weight
        
        # Add weights from items2
        for value, weight in items2:
            weight_map[value] += weight
        
        # Convert the dictionary to a sorted list of [value, weight] pairs
        result = sorted(weight_map.items(), key=lambda x: x[0])
        
        return result

def mergeSimilarItems(items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
    return Solution().mergeSimilarItems(items1, items2)