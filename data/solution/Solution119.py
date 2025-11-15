import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Initialize the row with 1s
        row = [1] * (rowIndex + 1)
        
        # Calculate each element of the row except the first and last
        for i in range(1, rowIndex):
            # Calculate from the end to the start to avoid overwriting
            for j in range(i, 0, -1):
                row[j] += row[j - 1]
        
        return row

def getRow(rowIndex: int) -> List[int]:
    return Solution().getRow(rowIndex)