import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = sum(nums)
        prefix_sum = 0
        result = []
        
        for i in range(n):
            current = nums[i]
            prefix_sum += current
            left_sum = i * current - prefix_sum + current
            right_sum = (total_sum - prefix_sum) - (n - i - 1) * current
            result.append(left_sum + right_sum)
        
        return result

def getSumAbsoluteDifferences(nums: List[int]) -> List[int]:
    return Solution().getSumAbsoluteDifferences(nums)