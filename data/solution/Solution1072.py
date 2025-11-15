import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # Dictionary to count the patterns of rows and their inverted patterns
        pattern_count = defaultdict(int)
        
        for row in matrix:
            # Convert row to a tuple for hashability
            original_pattern = tuple(row)
            # Create the inverted pattern of the row
            inverted_pattern = tuple(1 - cell for cell in row)
            
            # Increment the count of the original and inverted patterns
            pattern_count[original_pattern] += 1
            pattern_count[inverted_pattern] += 1
        
        # The result is the maximum count of any pattern
        return max(pattern_count.values())

def maxEqualRowsAfterFlips(matrix: List[List[int]]) -> int:
    return Solution().maxEqualRowsAfterFlips(matrix)