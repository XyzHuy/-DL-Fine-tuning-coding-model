import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by starting point. If two intervals have the same starting point, sort by ending point in descending order.
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        # Initialize the end of the previous interval
        prev_end = -1
        count = 0
        
        for start, end in intervals:
            # If the current interval is not covered by the previous one
            if end > prev_end:
                count += 1
                prev_end = end
        
        return count

def removeCoveredIntervals(intervals: List[List[int]]) -> int:
    return Solution().removeCoveredIntervals(intervals)