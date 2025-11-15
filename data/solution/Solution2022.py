import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Check if the total number of elements matches m * n
        if len(original) != m * n:
            return []
        
        # Construct the 2D array
        result = []
        for i in range(m):
            row = original[i * n:(i + 1) * n]
            result.append(row)
        
        return result

def construct2DArray(original: List[int], m: int, n: int) -> List[List[int]]:
    return Solution().construct2DArray(original, m, n)