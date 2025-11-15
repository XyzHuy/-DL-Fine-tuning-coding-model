import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # Find the leftmost occurrence of the target
        left_index = bisect.bisect_left(nums, target)
        # Find the rightmost occurrence of the target
        right_index = bisect.bisect_right(nums, target)
        # Calculate the number of occurrences of the target
        count = right_index - left_index
        # Check if the count is more than half the length of the array
        return count > len(nums) // 2

def isMajorityElement(nums: List[int], target: int) -> bool:
    return Solution().isMajorityElement(nums, target)