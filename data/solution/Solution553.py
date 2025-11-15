import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return f"{nums[0]}/{nums[1]}"
        
        # To maximize the result, we want to minimize the denominator.
        # This can be achieved by grouping all numbers after the first one in a single fraction.
        # For example, for nums = [a, b, c, d], the optimal division is a/(b/c/d) = a/((b/c)/d) = a/(b/(c*d))
        return f"{nums[0]}/({'/'.join(map(str, nums[1:]))})"

def optimalDivision(nums: List[int]) -> str:
    return Solution().optimalDivision(nums)