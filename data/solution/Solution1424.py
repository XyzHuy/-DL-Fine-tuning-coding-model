import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # Dictionary to hold the elements of the same diagonal
        diagonals = defaultdict(list)
        
        # Traverse the 2D list and group elements by their diagonal index (i + j)
        for i, row in enumerate(nums):
            for j, num in enumerate(row):
                diagonals[i + j].append(num)
        
        # Collect the elements in diagonal order
        result = []
        for diag in range(len(diagonals)):
            # The elements in each diagonal are traversed in reverse order
            result.extend(reversed(diagonals[diag]))
        
        return result

def findDiagonalOrder(nums: List[List[int]]) -> List[int]:
    return Solution().findDiagonalOrder(nums)