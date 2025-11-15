import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        num_dict = {}
        
        for num in nums:
            if num in num_dict:
                count += num_dict[num]
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        
        return count

def numIdenticalPairs(nums: List[int]) -> int:
    return Solution().numIdenticalPairs(nums)