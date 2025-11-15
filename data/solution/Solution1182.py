import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        # Create a dictionary to store the indices of each color
        color_indices = {1: [], 2: [], 3: []}
        
        for index, color in enumerate(colors):
            color_indices[color].append(index)
        
        def find_shortest_distance(index, color):
            if not color_indices[color]:
                return -1
            # Use binary search to find the closest index
            pos = bisect.bisect_left(color_indices[color], index)
            # Check the closest indices on both sides
            if pos == 0:
                return color_indices[color][0] - index
            if pos == len(color_indices[color]):
                return index - color_indices[color][-1]
            left = index - color_indices[color][pos - 1]
            right = color_indices[color][pos] - index
            return min(left, right)
        
        import bisect
        result = []
        for i, c in queries:
            result.append(find_shortest_distance(i, c))
        
        return result

def shortestDistanceColor(colors: List[int], queries: List[List[int]]) -> List[int]:
    return Solution().shortestDistanceColor(colors, queries)