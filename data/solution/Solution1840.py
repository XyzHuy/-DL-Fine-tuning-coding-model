import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # Add the initial condition
        restrictions = [[1, 0]] + restrictions
        # Sort restrictions by building index
        restrictions.sort()
        
        # Propagate right
        for i in range(1, len(restrictions)):
            idx1, height1 = restrictions[i - 1]
            idx2, height2 = restrictions[i]
            # Ensure the height difference constraint is not violated
            restrictions[i][1] = min(height2, height1 + (idx2 - idx1))
        
        # Propagate left
        for i in range(len(restrictions) - 2, -1, -1):
            idx1, height1 = restrictions[i]
            idx2, height2 = restrictions[i + 1]
            # Ensure the height difference constraint is not violated
            restrictions[i][1] = min(height1, height2 + (idx2 - idx1))
        
        # Calculate the maximum possible height
        max_height = 0
        for i in range(len(restrictions) - 1):
            idx1, height1 = restrictions[i]
            idx2, height2 = restrictions[i + 1]
            # Calculate the maximum height between two restricted buildings
            base_height = (height1 + height2 + idx2 - idx1) // 2
            max_height = max(max_height, base_height)
        
        # Check the height from the last restriction to the last building
        last_idx, last_height = restrictions[-1]
        max_height = max(max_height, last_height + n - last_idx)
        
        return max_height

def maxBuilding(n: int, restrictions: List[List[int]]) -> int:
    return Solution().maxBuilding(n, restrictions)