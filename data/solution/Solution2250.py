import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict
import bisect

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        # Create a dictionary to store lengths of rectangles grouped by their heights
        height_to_lengths = defaultdict(list)
        for l, h in rectangles:
            height_to_lengths[h].append(l)
        
        # Sort the lengths for each height
        for heights in height_to_lengths.values():
            heights.sort()
        
        # Initialize the result list
        result = []
        
        # For each point, count the number of rectangles that contain it
        for x, y in points:
            count = 0
            # Check all heights greater than or equal to y
            for h in range(y, 101):
                if h in height_to_lengths:
                    # Use binary search to find the number of lengths >= x
                    idx = bisect.bisect_left(height_to_lengths[h], x)
                    count += len(height_to_lengths[h]) - idx
            result.append(count)
        
        return result

def countRectangles(rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
    return Solution().countRectangles(rectangles, points)