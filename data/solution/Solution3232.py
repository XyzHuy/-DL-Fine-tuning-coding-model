import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum_single_digit = 0
        sum_double_digit = 0
        
        for num in nums:
            if num < 10:
                sum_single_digit += num
            else:
                sum_double_digit += num
        
        return sum_single_digit > sum_double_digit or sum_double_digit > sum_single_digit

def canAliceWin(nums: List[int]) -> bool:
    return Solution().canAliceWin(nums)