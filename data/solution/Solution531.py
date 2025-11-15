import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        if not picture or not picture[0]:
            return 0
        
        rows = len(picture)
        cols = len(picture[0])
        
        # Arrays to count the number of 'B's in each row and column
        row_count = [0] * rows
        col_count = [0] * cols
        
        # First pass: count 'B's in each row and column
        for i in range(rows):
            for j in range(cols):
                if picture[i][j] == 'B':
                    row_count[i] += 1
                    col_count[j] += 1
        
        # Second pass: find lonely 'B's
        lonely_pixel_count = 0
        for i in range(rows):
            for j in range(cols):
                if picture[i][j] == 'B' and row_count[i] == 1 and col_count[j] == 1:
                    lonely_pixel_count += 1
        
        return lonely_pixel_count

def findLonelyPixel(picture: List[List[str]]) -> int:
    return Solution().findLonelyPixel(picture)