import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        # Create a list of strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1
        
        # Join all rows to get the final string
        return ''.join(rows)

def convert(s: str, numRows: int) -> str:
    return Solution().convert(s, numRows)