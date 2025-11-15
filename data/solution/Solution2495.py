import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        last_even_index = -1
        count = 0
        
        for i, num in enumerate(nums):
            if num % 2 == 0:
                last_even_index = i
            count += last_even_index + 1
        
        return count

def evenProduct(nums: List[int]) -> int:
    return Solution().evenProduct(nums)