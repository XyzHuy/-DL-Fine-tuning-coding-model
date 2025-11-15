import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Voting Algorithm
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate

def majorityElement(nums: List[int]) -> int:
    return Solution().majorityElement(nums)