import random
import functools
import collections
import string
import math
import datetime


from typing import List
from bisect import bisect_left

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = []
        counts = []
        
        for num in reversed(nums):
            # Find the index where the number should be inserted to keep sorted_nums sorted
            index = bisect_left(sorted_nums, num)
            # The index is also the count of smaller elements to the right
            counts.append(index)
            # Insert the number into the sorted list
            sorted_nums.insert(index, num)
        
        # The counts are collected in reverse order, so reverse them back
        return counts[::-1]

def countSmaller(nums: List[int]) -> List[int]:
    return Solution().countSmaller(nums)