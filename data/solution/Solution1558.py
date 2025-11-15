import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        max_divide = 0
        
        for num in nums:
            divide_count = 0
            while num > 0:
                if num % 2 == 1:
                    operations += 1
                    num -= 1
                else:
                    divide_count += 1
                    num //= 2
            max_divide = max(max_divide, divide_count)
        
        return operations + max_divide

def minOperations(nums: List[int]) -> int:
    return Solution().minOperations(nums)