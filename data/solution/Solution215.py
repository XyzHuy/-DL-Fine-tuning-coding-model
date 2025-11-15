import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a min-heap with the first k elements
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        # Iterate over the remaining elements
        for num in nums[k:]:
            # If the current number is larger than the smallest in the heap, replace it
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        
        # The root of the heap is the kth largest element
        return min_heap[0]

def findKthLargest(nums: List[int], k: int) -> int:
    return Solution().findKthLargest(nums, k)