import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        current_value = 0
        
        for i, num in enumerate(nums):
            # Shift current_value to the left by 1 (equivalent to multiplying by 2)
            # and add the current bit (num)
            current_value = (current_value * 2 + num) % 5
            # Check if the current number (in base 10) is divisible by 5
            result.append(current_value == 0)
        
        return result

def prefixesDivBy5(nums: List[int]) -> List[bool]:
    return Solution().prefixesDivBy5(nums)