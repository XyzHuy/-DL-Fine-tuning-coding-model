import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1:
            return 0
        
        # Convert the list of sticks into a min-heap
        heapq.heapify(sticks)
        
        total_cost = 0
        
        # While there is more than one stick in the heap
        while len(sticks) > 1:
            # Pop the two smallest sticks
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)
            
            # The cost to combine these two sticks
            cost = first + second
            total_cost += cost
            
            # Push the combined stick back into the heap
            heapq.heappush(sticks, cost)
        
        return total_cost

def connectSticks(sticks: List[int]) -> int:
    return Solution().connectSticks(sticks)