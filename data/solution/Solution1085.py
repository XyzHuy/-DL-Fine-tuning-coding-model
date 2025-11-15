import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        # Find the minimum element in the list
        min_num = min(nums)
        
        # Calculate the sum of the digits of the minimum element
        digit_sum = sum(int(digit) for digit in str(min_num))
        
        # Return 0 if the sum is odd, otherwise return 1
        return 0 if digit_sum % 2 == 1 else 1

def sumOfDigits(nums: List[int]) -> int:
    return Solution().sumOfDigits(nums)