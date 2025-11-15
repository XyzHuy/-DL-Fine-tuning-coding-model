import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort intervals by the end point, and by the start point in descending order if end points are the same
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        # Initialize the result and the two most recent points added to the set
        result = 0
        first, second = -float('inf'), -float('inf')
        
        for start, end in intervals:
            # If the current interval does not cover the second point, we need to add two new points
            if start > second:
                first, second = end - 1, end
                result += 2
            # If the current interval covers the second point but not the first, we need to add one new point
            elif start > first:
                first, second = second, end
                result += 1
        
        return result

def intersectionSizeTwo(intervals: List[List[int]]) -> int:
    return Solution().intersectionSizeTwo(intervals)