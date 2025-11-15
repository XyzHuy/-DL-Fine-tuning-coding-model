import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


from sortedcontainers import SortedSet

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # This will store the numbers in a sorted order
        sorted_set = SortedSet()
        
        for i, num in enumerate(nums):
            # Find the smallest number >= nums[i] - valueDiff
            ceil_index = sorted_set.bisect_left(num - valueDiff)
            
            # Check if this number satisfies the condition abs(nums[i] - nums[j]) <= valueDiff
            if ceil_index < len(sorted_set) and sorted_set[ceil_index] <= num + valueDiff:
                return True
            
            # Add the current number to the sorted set
            sorted_set.add(num)
            
            # Maintain the window size of indexDiff
            if i >= indexDiff:
                sorted_set.remove(nums[i - indexDiff])
        
        return False

def containsNearbyAlmostDuplicate(nums: List[int], indexDiff: int, valueDiff: int) -> bool:
    return Solution().containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff)