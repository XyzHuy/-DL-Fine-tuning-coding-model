import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # The first element is always part of the cost
        first_element_cost = nums[0]
        
        # We need to find the two smallest elements after the first element
        # because these will be the starting elements of the second and third subarrays
        # to minimize the cost.
        remaining_elements = nums[1:]
        remaining_elements.sort()
        
        # The minimum cost will be the first element plus the two smallest elements from the rest
        return first_element_cost + remaining_elements[0] + remaining_elements[1]

def minimumCost(nums: List[int]) -> int:
    return Solution().minimumCost(nums)