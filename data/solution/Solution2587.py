import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # Sort the array in descending order
        nums.sort(reverse=True)
        
        # Initialize prefix sum and score
        prefix_sum = 0
        score = 0
        
        # Calculate prefix sums and count the number of positive integers
        for num in nums:
            prefix_sum += num
            if prefix_sum > 0:
                score += 1
            else:
                break
        
        return score

def maxScore(nums: List[int]) -> int:
    return Solution().maxScore(nums)