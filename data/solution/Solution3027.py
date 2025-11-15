import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Sort points by x-coordinate in ascending order.
        # If two points have the same x-coordinate, sort by y-coordinate in descending order.
        points.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        n = len(points)
        
        for i in range(n):
            max_y = float('-inf')
            for j in range(i + 1, n):
                # Check if points[j] can be Bob's position with points[i] as Alice's position
                if points[j][1] <= points[i][1] and points[j][1] > max_y:
                    count += 1
                    max_y = points[j][1]
        
        return count

def numberOfPairs(points: List[List[int]]) -> int:
    return Solution().numberOfPairs(points)