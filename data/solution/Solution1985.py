import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # Convert each string in nums to an integer and sort the list in descending order
        sorted_nums = sorted(nums, key=lambda x: int(x), reverse=True)
        # Return the k-th largest number as a string
        return sorted_nums[k-1]

def kthLargestNumber(nums: List[str], k: int) -> str:
    return Solution().kthLargestNumber(nums, k)