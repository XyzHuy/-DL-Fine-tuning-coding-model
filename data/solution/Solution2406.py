import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # Sort intervals by their start times
        intervals.sort()
        
        # Min-heap to keep track of the end times of the groups
        min_heap = []
        
        for interval in intervals:
            start, end = interval
            
            # If the interval doesn't overlap with the earliest ending interval, reuse that group
            if min_heap and min_heap[0] < start:
                heapq.heappop(min_heap)
            
            # Push the end time of the current interval onto the heap
            heapq.heappush(min_heap, end)
        
        # The size of the heap is the number of groups needed
        return len(min_heap)

def minGroups(intervals: List[List[int]]) -> int:
    return Solution().minGroups(intervals)