import random
import functools
import collections
import string
import math
import datetime


import heapq
from typing import List

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Convert all pile sizes to negative and push them into a heap
        max_heap = [-pile for pile in piles]
        heapq.heapify(max_heap)
        
        # Perform k operations
        for _ in range(k):
            # Pop the largest pile (smallest negative number)
            largest_pile = heapq.heappop(max_heap)
            # Remove floor(largest_pile / 2) stones
            largest_pile += -largest_pile // 2
            # Push the updated pile size back into the heap
            heapq.heappush(max_heap, largest_pile)
        
        # Sum up the absolute values of the heap to get the total number of stones remaining
        return -sum(max_heap)

def minStoneSum(piles: List[int], k: int) -> int:
    return Solution().minStoneSum(piles, k)