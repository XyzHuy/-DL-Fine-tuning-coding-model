import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        # Remove duplicates and sort the array
        unique_nums = sorted(set(nums))
        
        min_operations = n
        for i, num in enumerate(unique_nums):
            # Find the position where num + n - 1 would fit in the sorted unique list
            idx = bisect.bisect_right(unique_nums, num + n - 1)
            # The number of elements already in the range [num, num + n - 1]
            in_range = idx - i
            # The number of operations needed to make the array continuous
            operations = n - in_range
            min_operations = min(min_operations, operations)
        
        return min_operations

def minOperations(nums: List[int]) -> int:
    return Solution().minOperations(nums)