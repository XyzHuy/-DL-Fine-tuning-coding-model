import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        # Count how many numbers have at least one trailing zero in their binary representation
        count_even = 0
        for num in nums:
            if num & 1 == 0:  # Check if the number is even (has at least one trailing zero)
                count_even += 1
            if count_even >= 2:  # If we find at least two such numbers, return True
                return True
        return False  # If less than two numbers have trailing zeros, return False

def hasTrailingZeros(nums: List[int]) -> bool:
    return Solution().hasTrailingZeros(nums)