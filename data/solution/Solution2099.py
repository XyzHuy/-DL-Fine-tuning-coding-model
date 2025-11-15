import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Create a list of tuples (value, index) from nums
        indexed_nums = list(enumerate(nums))
        
        # Use a heap to find the k largest elements based on their values
        # We use a min-heap of size k to keep track of the largest elements
        min_heap = []
        for index, value in indexed_nums:
            heapq.heappush(min_heap, (value, index))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # Extract the elements and their indices from the heap
        # and sort them by their original index to maintain order
        min_heap.sort(key=lambda x: x[1])
        
        # Extract the values from the sorted heap
        result = [value for value, index in min_heap]
        
        return result

def maxSubsequence(nums: List[int], k: int) -> List[int]:
    return Solution().maxSubsequence(nums, k)