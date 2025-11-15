import random
import functools
import collections
import string
import math
import datetime


import heapq
from typing import List

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        target = total_sum / 2
        current_sum = total_sum
        operations = 0
        
        # Create a max-heap by pushing negative values
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        while current_sum > target:
            # Extract the largest element (negate it to get the original value)
            largest = -heapq.heappop(max_heap)
            # Halve the largest element
            largest /= 2
            # Push the halved value back into the heap (negate it)
            heapq.heappush(max_heap, -largest)
            # Update the current sum
            current_sum -= largest
            # Increment the operation count
            operations += 1
        
        return operations

def halveArray(nums: List[int]) -> int:
    return Solution().halveArray(nums)