import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        if not picture or not picture[0]:
            return 0
        
        m, n = len(picture), len(picture[0])
        row_count = [0] * m
        col_count = [0] * n
        col_to_rows = defaultdict(list)
        
        # Count black pixels in each row and column
        for r in range(m):
            for c in range(n):
                if picture[r][c] == 'B':
                    row_count[r] += 1
                    col_count[c] += 1
                    col_to_rows[c].append(r)
        
        lonely_pixels = 0
        
        for r in range(m):
            for c in range(n):
                if picture[r][c] == 'B' and row_count[r] == target and col_count[c] == target:
                    # Check if all rows with a black pixel at column c are the same as row r
                    if all(picture[r] == picture[rr] for rr in col_to_rows[c]):
                        lonely_pixels += 1
        
        return lonely_pixels

def findBlackPixel(picture: List[List[str]], target: int) -> int:
    return Solution().findBlackPixel(picture, target)