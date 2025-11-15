import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert all stone weights to negative to use min-heap as max-heap
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            # Pop the two heaviest stones
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            
            if first != second:
                # Push the difference back into the heap
                heapq.heappush(stones, -(first - second))
        
        # If there's a stone left, return its weight, otherwise return 0
        return -stones[0] if stones else 0

def lastStoneWeight(stones: List[int]) -> int:
    return Solution().lastStoneWeight(stones)