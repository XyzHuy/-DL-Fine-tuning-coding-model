import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        max_score = float('-inf')
        
        for num in nums:
            left_sum += num
            max_score = max(max_score, left_sum, total_sum - left_sum + num)
        
        return max_score

def maximumSumScore(nums: List[int]) -> int:
    return Solution().maximumSumScore(nums)