import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Convert nums into a max-heap by pushing the negative of each element
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        score = 0
        for _ in range(k):
            # Pop the largest element (smallest negative)
            largest = -heapq.heappop(max_heap)
            # Increase the score by the largest element
            score += largest
            # Replace the element with its ceiling after dividing by 3
            new_value = math.ceil(largest / 3)
            # Push the new value back into the heap (as negative)
            heapq.heappush(max_heap, -new_value)
        
        return score

def maxKelements(nums: List[int], k: int) -> int:
    return Solution().maxKelements(nums, k)