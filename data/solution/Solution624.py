import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Initialize the minimum and maximum values from the first array
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0
        
        # Iterate over the remaining arrays
        for i in range(1, len(arrays)):
            current_array = arrays[i]
            current_min = current_array[0]
            current_max = current_array[-1]
            
            # Calculate the potential maximum distance with the current array
            max_distance = max(max_distance, abs(current_max - min_val), abs(max_val - current_min))
            
            # Update the global minimum and maximum values
            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)
        
        return max_distance

def maxDistance(arrays: List[List[int]]) -> int:
    return Solution().maxDistance(arrays)