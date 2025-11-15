import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Create a list of tuples (start, original_index)
        start_intervals = sorted((interval[0], i) for i, interval in enumerate(intervals))
        
        result = []
        for interval in intervals:
            # Use bisect to find the smallest start that is >= end of the current interval
            idx = bisect.bisect_left(start_intervals, (interval[1],))
            if idx < len(start_intervals):
                result.append(start_intervals[idx][1])
            else:
                result.append(-1)
        
        return result

def findRightInterval(intervals: List[List[int]]) -> List[int]:
    return Solution().findRightInterval(intervals)