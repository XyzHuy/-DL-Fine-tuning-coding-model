import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        # Transform peaks to [left_boundary, right_boundary]
        mountains = [(x - y, x + y) for x, y in peaks]
        
        # Sort mountains by left boundary, and by right boundary in descending order if left boundaries are the same
        mountains.sort(key=lambda m: (m[0], -m[1]))
        
        visible_count = 0
        max_right = float('-inf')
        
        for i in range(len(mountains)):
            left, right = mountains[i]
            
            # If the current mountain is completely covered by the previous one, it's not visible
            if right <= max_right:
                continue
            
            # If the current mountain is not covered, it's visible
            visible_count += 1
            max_right = right
            
            # Check for duplicate peaks
            if i + 1 < len(mountains) and mountains[i] == mountains[i + 1]:
                # If the next mountain is the same, they completely overlap, so both are not visible
                visible_count -= 1
                # Skip the next mountain since it's a duplicate
                while i + 1 < len(mountains) and mountains[i] == mountains[i + 1]:
                    i += 1
        
        return visible_count

def visibleMountains(peaks: List[List[int]]) -> int:
    return Solution().visibleMountains(peaks)