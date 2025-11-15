import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # Helper function to calculate squared distance between two points
        def dist2(p, q):
            return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
        
        # Calculate all six possible squared distances between the points
        distances = [
            dist2(p1, p2), dist2(p1, p3), dist2(p1, p4),
            dist2(p2, p3), dist2(p2, p4), dist2(p3, p4)
        ]
        
        # Count the frequency of each distance
        distance_count = Counter(distances)
        
        # A valid square should have four equal sides and two equal diagonals
        # So the distance count should be two unique values, one with frequency 4 (sides) and one with frequency 2 (diagonals)
        return len(distance_count) == 2 and 2 in distance_count.values() and 4 in distance_count.values()

def validSquare(p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
    return Solution().validSquare(p1, p2, p3, p4)