import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals by their start time
        intervals.sort()
        # Sort queries while keeping track of their original indices
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        
        min_heap = []  # This will store (interval_size, end_time) pairs
        result = [-1] * len(queries)
        interval_index = 0
        
        for query_index, query in sorted_queries:
            # Add intervals that start before or at the query point
            while interval_index < len(intervals) and intervals[interval_index][0] <= query:
                start, end = intervals[interval_index]
                heapq.heappush(min_heap, (end - start + 1, end))
                interval_index += 1
            
            # Remove intervals that end before the query point
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            
            # The smallest interval that contains the query point
            if min_heap:
                result[query_index] = min_heap[0][0]
        
        return result

def minInterval(intervals: List[List[int]], queries: List[int]) -> List[int]:
    return Solution().minInterval(intervals, queries)