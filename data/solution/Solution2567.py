import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # Sort the array to easily find the smallest and largest elements
        nums.sort()
        
        # There are three possible strategies to minimize the score:
        # 1. Change the two largest elements
        # 2. Change the two smallest elements
        # 3. Change one smallest and one largest element
        # We need to calculate the score for each strategy and choose the minimum
        
        # Strategy 1: Change the two largest elements
        score1 = nums[-3] - nums[0]
        
        # Strategy 2: Change the two smallest elements
        score2 = nums[-1] - nums[2]
        
        # Strategy 3: Change one smallest and one largest element
        score3 = nums[-2] - nums[1]
        
        # Return the minimum score among the three strategies
        return min(score1, score2, score3)

def minimizeSum(nums: List[int]) -> int:
    return Solution().minimizeSum(nums)