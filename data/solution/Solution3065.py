import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Count the number of elements in nums that are less than k
        operations = sum(1 for num in nums if num < k)
        return operations

def minOperations(nums: List[int], k: int) -> int:
    return Solution().minOperations(nums, k)