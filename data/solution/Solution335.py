import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        # If there are less than 4 lines, it cannot cross itself
        if len(distance) < 4:
            return False
        
        # Iterate through the distance array starting from the 4th element
        for i in range(3, len(distance)):
            # Case 1: The current line crosses the line 3 steps ahead
            if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
                return True
            # Case 2: The current line crosses the line 4 steps ahead
            if i >= 4 and distance[i - 1] == distance[i - 3] and distance[i] + distance[i - 4] >= distance[i - 2]:
                return True
            # Case 3: The current line crosses the line 5 steps ahead
            if i >= 5 and distance[i - 2] >= distance[i - 4] and distance[i - 3] >= distance[i - 1] and distance[i] + distance[i - 4] >= distance[i - 2] and distance[i - 1] + distance[i - 5] >= distance[i - 3]:
                return True
        
        return False

def isSelfCrossing(distance: List[int]) -> bool:
    return Solution().isSelfCrossing(distance)