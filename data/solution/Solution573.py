import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        def distance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        total_distance = 0
        min_extra_distance = float('inf')
        
        for nut in nuts:
            total_distance += 2 * distance(nut, tree)
            # Calculate the extra distance if the squirrel picks this nut first
            extra_distance = distance(squirrel, nut) - distance(nut, tree)
            min_extra_distance = min(min_extra_distance, extra_distance)
        
        return total_distance + min_extra_distance

def minDistance(height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
    return Solution().minDistance(height, width, tree, squirrel, nuts)