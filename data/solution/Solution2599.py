import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        prefix_sum = 0
        operations = 0
        min_heap = []
        
        for num in nums:
            # Add the current number to the prefix sum
            prefix_sum += num
            
            # If the prefix sum becomes negative, we need to remove the smallest negative number
            if prefix_sum < 0:
                # Push the negative of the current number onto the min-heap
                heapq.heappush(min_heap, num)
                # Pop the smallest negative number from the heap
                smallest_negative = heapq.heappop(min_heap)
                # Adjust the prefix sum by removing the smallest negative number
                prefix_sum -= smallest_negative
                # Increment the operation count
                operations += 1
            else:
                # If the current number is negative, push it onto the heap for future use
                if num < 0:
                    heapq.heappush(min_heap, num)
        
        return operations

def makePrefSumNonNegative(nums: List[int]) -> int:
    return Solution().makePrefSumNonNegative(nums)