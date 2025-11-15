import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        m = len(queries)
        ans = [-1] * m
        
        # Process each query
        for i, (a, b) in enumerate(queries):
            # If Alice and Bob are already in the same building or Alice can directly move to Bob's building
            if a == b or (a < b and heights[a] < heights[b]) or (b < a and heights[b] < heights[a]):
                ans[i] = max(a, b)
                continue
        
        # Dictionary to hold queries that need to be processed for each building index
        pending_queries = [[] for _ in range(n)]
        
        # Populate the pending_queries dictionary
        for i, (a, b) in enumerate(queries):
            if ans[i] == -1:
                # Ensure a is the smaller index
                if a > b:
                    a, b = b, a
                # Add the query to the pending list of the larger index
                pending_queries[b].append((heights[a], i))
        
        # Min-heap to keep track of the next possible building heights
        min_heap = []
        
        # Process buildings from left to right
        for j in range(n):
            # Add all buildings that are taller than the current building to the heap
            while min_heap and min_heap[0][0] < heights[j]:
                _, query_index = heapq.heappop(min_heap)
                ans[query_index] = j
            
            # Add the current building to the heap for future queries
            for height, query_index in pending_queries[j]:
                heapq.heappush(min_heap, (height, query_index))
        
        return ans

def leftmostBuildingQueries(heights: List[int], queries: List[List[int]]) -> List[int]:
    return Solution().leftmostBuildingQueries(heights, queries)