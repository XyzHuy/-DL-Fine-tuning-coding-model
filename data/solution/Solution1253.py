import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        result = [[0] * n for _ in range(2)]
        
        # Iterate through the colsum to decide the placement of 1s and 2s
        for i in range(n):
            if colsum[i] == 2:
                result[0][i] = 1
                result[1][i] = 1
                upper -= 1
                lower -= 1
            elif colsum[i] == 1:
                if upper > lower:
                    result[0][i] = 1
                    upper -= 1
                else:
                    result[1][i] = 1
                    lower -= 1
        
        # Check if we have used exactly the required number of 1s in both rows
        if upper != 0 or lower != 0:
            return []
        
        return result

def reconstructMatrix(upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
    return Solution().reconstructMatrix(upper, lower, colsum)