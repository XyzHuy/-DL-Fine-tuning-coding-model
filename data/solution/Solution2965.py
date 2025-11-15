import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        expected_sum = n * n * (n * n + 1) // 2
        actual_sum = 0
        num_count = Counter()
        
        for row in grid:
            for num in row:
                actual_sum += num
                num_count[num] += 1
        
        repeated_num = 0
        missing_num = 0
        
        for num in range(1, n * n + 1):
            if num_count[num] == 2:
                repeated_num = num
            elif num_count[num] == 0:
                missing_num = num
        
        return [repeated_num, missing_num]

def findMissingAndRepeatedValues(grid: List[List[int]]) -> List[int]:
    return Solution().findMissingAndRepeatedValues(grid)