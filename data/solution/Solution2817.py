import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


from sortedcontainers import SortedList
from typing import List

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        # Initialize the sorted list to keep track of elements at least x indices apart
        sorted_list = SortedList()
        min_diff = float('inf')
        
        # Iterate through the array starting from the x-th element
        for i in range(x, len(nums)):
            # Add the element that is x indices behind the current element to the sorted list
            sorted_list.add(nums[i - x])
            
            # Find the position where the current element would fit in the sorted list
            pos = sorted_list.bisect_left(nums[i])
            
            # Check the element just before the insertion point
            if pos > 0:
                min_diff = min(min_diff, nums[i] - sorted_list[pos - 1])
            
            # Check the element at the insertion point
            if pos < len(sorted_list):
                min_diff = min(min_diff, sorted_list[pos] - nums[i])
        
        return min_diff

def minAbsoluteDifference(nums: List[int], x: int) -> int:
    return Solution().minAbsoluteDifference(nums, x)