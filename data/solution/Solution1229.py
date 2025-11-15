import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # Sort both slots by start time
        slots1.sort()
        slots2.sort()
        
        i, j = 0, 0
        
        # Iterate over both slots
        while i < len(slots1) and j < len(slots2):
            # Find the intersection of the two slots
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            
            # Check if the intersection is at least the duration long
            if end - start >= duration:
                return [start, start + duration]
            
            # Move the pointer that has the earlier end time
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        
        # If no common slot is found
        return []

def minAvailableDuration(slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
    return Solution().minAvailableDuration(slots1, slots2, duration)