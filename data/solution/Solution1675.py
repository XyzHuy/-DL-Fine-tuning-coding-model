import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # Convert all numbers to their maximum possible even value
        max_heap = []
        min_val = float('inf')
        for num in nums:
            if num % 2 == 1:
                num *= 2
            heapq.heappush(max_heap, -num)
            min_val = min(min_val, num)
        
        # Calculate the initial deviation
        min_deviation = -max_heap[0] - min_val
        
        # Reduce the maximum element until it becomes odd
        while max_heap[0] % 2 == 0:
            max_val = -heapq.heappop(max_heap)
            new_val = max_val // 2
            min_val = min(min_val, new_val)
            heapq.heappush(max_heap, -new_val)
            min_deviation = min(min_deviation, -max_heap[0] - min_val)
        
        return min_deviation

def minimumDeviation(nums: List[int]) -> int:
    return Solution().minimumDeviation(nums)