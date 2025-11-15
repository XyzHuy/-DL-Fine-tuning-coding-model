import random
import functools
import collections
import string
import math
import datetime


from sortedcontainers import SortedList
from typing import List

class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        prefix_sum = 0
        prefix_count = SortedList([0])  # Start with a prefix sum of 0
        count = 0
        
        for num in nums:
            if num == 1:
                prefix_sum += 1
            else:
                prefix_sum -= 1
            
            # Find the number of prefix sums less than the current prefix sum
            count += prefix_count.bisect_left(prefix_sum)
            count %= MOD
            
            # Add the current prefix sum to the sorted list
            prefix_count.add(prefix_sum)
        
        return count

def subarraysWithMoreZerosThanOnes(nums: List[int]) -> int:
    return Solution().subarraysWithMoreZerosThanOnes(nums)