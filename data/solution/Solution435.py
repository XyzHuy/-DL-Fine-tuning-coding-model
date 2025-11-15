import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals by their end time
        intervals.sort(key=lambda x: x[1])
        
        # Initialize the end time of the last added interval
        last_end = intervals[0][1]
        # Initialize the count of intervals to remove
        remove_count = 0
        
        # Iterate through the intervals starting from the second one
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start >= last_end:
                # If the current interval does not overlap, update the last end time
                last_end = end
            else:
                # If the current interval overlaps, increment the remove count
                remove_count += 1
        
        return remove_count

def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    return Solution().eraseOverlapIntervals(intervals)