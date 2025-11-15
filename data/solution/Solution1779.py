import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float('inf')
        min_index = -1
        
        for index, (px, py) in enumerate(points):
            if px == x or py == y:  # Check if the point is valid
                distance = abs(x - px) + abs(y - py)
                if distance < min_distance:
                    min_distance = distance
                    min_index = index
        
        return min_index

def nearestValidPoint(x: int, y: int, points: List[List[int]]) -> int:
    return Solution().nearestValidPoint(x, y, points)