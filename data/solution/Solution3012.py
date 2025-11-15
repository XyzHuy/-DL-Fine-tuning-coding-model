import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        # Find the minimum element in the array
        min_num = min(nums)
        
        # Check if there is any element in the array that gives a non-zero remainder when divided by min_num
        non_zero_remainder_exists = any(num % min_num != 0 for num in nums)
        
        # If such an element exists, we can reduce the array to a single element
        if non_zero_remainder_exists:
            return 1
        
        # Otherwise, count the number of times the minimum element appears in the array
        min_count = nums.count(min_num)
        
        # The minimum length of the array will be (min_count + 1) // 2
        return (min_count + 1) // 2

def minimumArrayLength(nums: List[int]) -> int:
    return Solution().minimumArrayLength(nums)