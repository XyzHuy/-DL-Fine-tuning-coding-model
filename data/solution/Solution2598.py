import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # Calculate the remainder of each number when divided by value
        remainders = [num % value for num in nums]
        
        # Count the frequency of each remainder
        remainder_count = Counter(remainders)
        
        # Find the smallest integer that cannot be formed
        for i in range(len(nums) + 1):
            remainder = i % value
            if remainder_count[remainder] == 0:
                return i
            remainder_count[remainder] -= 1
        
        return len(nums)

def findSmallestInteger(nums: List[int], value: int) -> int:
    return Solution().findSmallestInteger(nums, value)