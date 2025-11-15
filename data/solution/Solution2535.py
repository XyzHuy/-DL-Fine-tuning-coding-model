import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        # Calculate the element sum
        element_sum = sum(nums)
        
        # Calculate the digit sum
        digit_sum = sum(int(digit) for num in nums for digit in str(num))
        
        # Return the absolute difference between element sum and digit sum
        return abs(element_sum - digit_sum)

def differenceOfSum(nums: List[int]) -> int:
    return Solution().differenceOfSum(nums)