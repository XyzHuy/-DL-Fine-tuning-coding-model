import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Base case: the power set of an empty set is a set containing the empty set
        if not nums:
            return [[]]
        
        # Recursive case: get the subsets of the rest of the numbers
        rest_subsets = self.subsets(nums[1:])
        
        # For each subset, add the current number to create new subsets
        with_current = [[nums[0]] + subset for subset in rest_subsets]
        
        # Return the combination of subsets with and without the current number
        return rest_subsets + with_current

def subsets(nums: List[int]) -> List[List[int]]:
    return Solution().subsets(nums)