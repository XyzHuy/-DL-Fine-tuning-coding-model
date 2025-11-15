import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quadratic(x):
            return a * x * x + b * x + c
        
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        fill_index = n - 1 if a >= 0 else 0
        
        while left <= right:
            left_val = quadratic(nums[left])
            right_val = quadratic(nums[right])
            
            if (a >= 0 and left_val > right_val) or (a < 0 and left_val < right_val):
                result[fill_index] = left_val
                left += 1
            else:
                result[fill_index] = right_val
                right -= 1
            
            fill_index += 1 if a < 0 else -1
        
        return result

def sortTransformedArray(nums: List[int], a: int, b: int, c: int) -> List[int]:
    return Solution().sortTransformedArray(nums, a, b, c)