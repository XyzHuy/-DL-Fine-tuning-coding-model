import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # Initialize the sign as positive
        sign = 1
        
        # Iterate through each number in the array
        for num in nums:
            if num == 0:
                # If any number is zero, the product is zero
                return 0
            elif num < 0:
                # Flip the sign for each negative number
                sign *= -1
        
        # Return the final sign
        return sign

def arraySign(nums: List[int]) -> int:
    return Solution().arraySign(nums)