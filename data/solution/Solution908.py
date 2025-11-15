import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        # Calculate the current maximum and minimum values in the list
        max_val = max(nums)
        min_val = min(nums)
        
        # The best we can do is to reduce the difference between max and min by 2*k
        # If the reduced difference is less than or equal to 0, the score can be 0
        return max(0, max_val - min_val - 2 * k)

def smallestRangeI(nums: List[int], k: int) -> int:
    return Solution().smallestRangeI(nums, k)