import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        # Use a min-heap to always increment the smallest element
        heapq.heapify(nums)
        
        # Perform k operations
        for _ in range(k):
            # Pop the smallest element, increment it, and push it back
            smallest = heapq.heappop(nums)
            heapq.heappush(nums, smallest + 1)
        
        # Calculate the product of the elements in the heap
        product = 1
        MOD = 10**9 + 7
        for num in nums:
            product = (product * num) % MOD
        
        return product

def maximumProduct(nums: List[int], k: int) -> int:
    return Solution().maximumProduct(nums, k)