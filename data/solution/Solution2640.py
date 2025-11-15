import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        max_so_far = 0
        conversion_sum = 0
        result = []
        
        for num in nums:
            max_so_far = max(max_so_far, num)
            conversion_value = num + max_so_far
            conversion_sum += conversion_value
            result.append(conversion_sum)
        
        return result

def findPrefixScore(nums: List[int]) -> List[int]:
    return Solution().findPrefixScore(nums)