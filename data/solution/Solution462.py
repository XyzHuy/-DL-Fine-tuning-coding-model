import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # Find the median
        median = sorted(nums)[len(nums) // 2]
        
        # Calculate the total number of moves required to make all elements equal to the median
        moves = sum(abs(num - median) for num in nums)
        
        return moves

def minMoves2(nums: List[int]) -> int:
    return Solution().minMoves2(nums)