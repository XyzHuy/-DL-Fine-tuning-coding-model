import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        # Convert blocks list into a min-heap
        heapq.heapify(blocks)
        
        # While there is more than one block, we need to use the two smallest blocks
        while len(blocks) > 1:
            # Pop the two smallest elements
            first_min = heapq.heappop(blocks)
            second_min = heapq.heappop(blocks)
            
            # The time to build these two blocks is the split time plus the time to build the larger block
            combined_time = split + second_min
            
            # Push the combined time back into the heap
            heapq.heappush(blocks, combined_time)
        
        # The root of the heap is the minimum time needed to build all blocks
        return blocks[0]

def minBuildTime(blocks: List[int], split: int) -> int:
    return Solution().minBuildTime(blocks, split)