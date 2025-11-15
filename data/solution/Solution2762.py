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
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_list = SortedList()
        left = 0
        result = 0
        
        for right in range(n):
            sorted_list.add(nums[right])
            
            # Ensure the condition |max - min| <= 2 is satisfied
            while sorted_list and sorted_list[-1] - sorted_list[0] > 2:
                sorted_list.remove(nums[left])
                left += 1
            
            # All subarrays ending at 'right' and starting from any index between 'left' and 'right' are valid
            result += right - left + 1
        
        return result

def continuousSubarrays(nums: List[int]) -> int:
    return Solution().continuousSubarrays(nums)