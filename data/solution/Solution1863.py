import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(start, current_xor):
            # Add the current XOR total of the subset to the result
            self.result += current_xor
            # Iterate over the remaining elements to generate subsets
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset and move to the next element
                backtrack(i + 1, current_xor ^ nums[i])
        
        self.result = 0
        backtrack(0, 0)
        return self.result

def subsetXORSum(nums: List[int]) -> int:
    return Solution().subsetXORSum(nums)