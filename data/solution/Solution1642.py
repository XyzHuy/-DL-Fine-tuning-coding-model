import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        # Min-heap to store the largest jumps where we used bricks
        ladder_heap = []
        
        for i in range(n - 1):
            height_diff = heights[i + 1] - heights[i]
            
            if height_diff > 0:
                # Push the current height difference into the min-heap
                heapq.heappush(ladder_heap, height_diff)
                
                # If the number of elements in the heap exceeds the number of ladders,
                # we need to use bricks for the smallest height difference
                if len(ladder_heap) > ladders:
                    # Use bricks for the smallest height difference
                    bricks -= heapq.heappop(ladder_heap)
                
                # If at any point we do not have enough bricks, return the current index
                if bricks < 0:
                    return i
        
        # If we can reach the last building, return the last index
        return n - 1

def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    return Solution().furthestBuilding(heights, bricks, ladders)