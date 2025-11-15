import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Sets to keep track of unique lamps
        lamp_set = set()
        # Dictionaries to count the number of lamps illuminating rows, columns, and diagonals
        row_count = defaultdict(int)
        col_count = defaultdict(int)
        diag_count = defaultdict(int)
        anti_diag_count = defaultdict(int)
        
        # Initialize the counts based on the given lamps
        for r, c in lamps:
            if (r, c) not in lamp_set:
                lamp_set.add((r, c))
                row_count[r] += 1
                col_count[c] += 1
                diag_count[r - c] += 1
                anti_diag_count[r + c] += 1
        
        # Result array
        result = []
        
        # Directions for the lamp and its adjacent cells
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Process each query
        for r, c in queries:
            # Check if the cell is illuminated
            if row_count[r] > 0 or col_count[c] > 0 or diag_count[r - c] > 0 or anti_diag_count[r + c] > 0:
                result.append(1)
            else:
                result.append(0)
            
            # Turn off the lamp at the queried cell and its adjacent cells
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in lamp_set:
                    lamp_set.remove((nr, nc))
                    row_count[nr] -= 1
                    col_count[nc] -= 1
                    diag_count[nr - nc] -= 1
                    anti_diag_count[nr + nc] -= 1
        
        return result

def gridIllumination(n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
    return Solution().gridIllumination(n, lamps, queries)