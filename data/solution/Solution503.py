import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []
        
        # We iterate over the list twice to simulate the circular array
        for i in range(n * 2):
            # Use modulo to wrap around the array
            while stack and nums[stack[-1]] < nums[i % n]:
                result[stack.pop()] = nums[i % n]
            # Only push the index in the first pass
            if i < n:
                stack.append(i)
        
        return result

def nextGreaterElements(nums: List[int]) -> List[int]:
    return Solution().nextGreaterElements(nums)