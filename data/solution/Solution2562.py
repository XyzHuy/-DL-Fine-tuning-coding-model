import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concatenation_value = 0
        while nums:
            if len(nums) > 1:
                first = nums.pop(0)
                last = nums.pop()
                concatenated = int(str(first) + str(last))
                concatenation_value += concatenated
            else:
                concatenation_value += nums.pop()
        return concatenation_value

def findTheArrayConcVal(nums: List[int]) -> int:
    return Solution().findTheArrayConcVal(nums)