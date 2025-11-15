import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        # Sort each row in descending order
        for row in nums:
            row.sort(reverse=True)
        
        score = 0
        # Iterate over each column index
        for col in range(len(nums[0])):
            # Find the maximum value in the current column
            max_in_col = max(nums[row][col] for row in range(len(nums)))
            # Add the maximum value to the score
            score += max_in_col
        
        return score

def matrixSum(nums: List[List[int]]) -> int:
    return Solution().matrixSum(nums)