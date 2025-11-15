import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_len = 0
        pos_length = 0
        neg_length = 0
        
        for num in nums:
            if num == 0:
                pos_length = 0
                neg_length = 0
            elif num > 0:
                pos_length += 1
                neg_length = neg_length + 1 if neg_length > 0 else 0
            else:
                new_pos_length = neg_length + 1 if neg_length > 0 else 0
                neg_length = pos_length + 1
                pos_length = new_pos_length
            
            max_len = max(max_len, pos_length)
        
        return max_len

def getMaxLen(nums: List[int]) -> int:
    return Solution().getMaxLen(nums)