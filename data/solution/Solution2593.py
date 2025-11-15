import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        marked = [False] * len(nums)
        
        # Create a list of tuples (value, index) and sort it
        indexed_nums = sorted((num, idx) for idx, num in enumerate(nums))
        
        for num, idx in indexed_nums:
            if not marked[idx]:
                score += num
                # Mark the current element and its adjacent elements
                marked[idx] = True
                if idx > 0:
                    marked[idx - 1] = True
                if idx < len(nums) - 1:
                    marked[idx + 1] = True
        
        return score

def findScore(nums: List[int]) -> int:
    return Solution().findScore(nums)