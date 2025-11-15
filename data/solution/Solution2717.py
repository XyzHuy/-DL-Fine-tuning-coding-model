import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        index_of_1 = nums.index(1)
        index_of_n = nums.index(n)
        
        # Calculate the number of swaps needed to move 1 to the start
        swaps_to_start = index_of_1
        
        # Calculate the number of swaps needed to move n to the end
        swaps_to_end = n - 1 - index_of_n
        
        # If 1 is already after n, we have counted one swap too many
        if index_of_1 > index_of_n:
            swaps_to_end -= 1
        
        return swaps_to_start + swaps_to_end

def semiOrderedPermutation(nums: List[int]) -> int:
    return Solution().semiOrderedPermutation(nums)