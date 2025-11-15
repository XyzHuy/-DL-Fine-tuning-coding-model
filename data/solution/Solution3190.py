import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        remainder_count = [0, 0, 0]
        
        for num in nums:
            remainder_count[num % 3] += 1
        
        # We need to make all numbers have a remainder of 0 when divided by 3
        # The optimal strategy is to convert numbers with remainder 1 to 0 or 2
        # and numbers with remainder 2 to 0 or 1
        # We should choose the conversion that results in the minimum operations
        
        # If all numbers are already divisible by 3, no operations are needed
        if remainder_count[1] == 0 and remainder_count[2] == 0:
            return 0
        
        # Calculate the minimum operations needed
        # We can either convert all 1s to 0s and all 2s to 0s
        # Or convert all 1s to 2s and all 2s to 1s
        return min(remainder_count[1] + remainder_count[2], 
                   remainder_count[1] * 2 + remainder_count[2] * 2)

def minimumOperations(nums: List[int]) -> int:
    return Solution().minimumOperations(nums)