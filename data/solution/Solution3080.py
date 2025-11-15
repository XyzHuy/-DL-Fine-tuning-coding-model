import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Initialize a min-heap with (value, index) pairs
        min_heap = [(value, index) for index, value in enumerate(nums)]
        heapq.heapify(min_heap)
        
        # Initialize a set to keep track of marked indices
        marked_indices = set()
        
        # Calculate the initial sum of all elements
        current_sum = sum(nums)
        
        # Result list to store the sum of unmarked elements after each query
        result = []
        
        # Process each query
        for index, k in queries:
            # Mark the element at the specified index if not already marked
            if index not in marked_indices:
                marked_indices.add(index)
                current_sum -= nums[index]
            
            # Mark k smallest unmarked elements
            while k > 0 and min_heap:
                value, idx = heapq.heappop(min_heap)
                if idx not in marked_indices:
                    marked_indices.add(idx)
                    current_sum -= value
                    k -= 1
            
            # Append the current sum of unmarked elements to the result list
            result.append(current_sum)
        
        return result

def unmarkedSumArray(nums: List[int], queries: List[List[int]]) -> List[int]:
    return Solution().unmarkedSumArray(nums, queries)