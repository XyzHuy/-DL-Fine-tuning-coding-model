import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals based on the starting point
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # If merged list is empty or current interval does not overlap with the last merged interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There is an overlap, so merge the current interval with the last merged interval
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged

def merge(intervals: List[List[int]]) -> List[List[int]]:
    return Solution().merge(intervals)