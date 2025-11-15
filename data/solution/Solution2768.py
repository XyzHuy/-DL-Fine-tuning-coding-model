import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict
from typing import List

class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        # Dictionary to count the number of black cells in each 2x2 block
        block_count = defaultdict(int)
        
        # For each black cell, update the count of black cells in the relevant 2x2 blocks
        for x, y in coordinates:
            for dx, dy in [(0, 0), (0, -1), (-1, 0), (-1, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m - 1 and 0 <= ny < n - 1:
                    block_count[(nx, ny)] += 1
        
        # Initialize the result array with 0s
        result = [0] * 5
        
        # Count the number of blocks with exactly i black cells
        for count in block_count.values():
            result[count] += 1
        
        # The number of blocks with 0 black cells is the total number of 2x2 blocks minus the counted ones
        total_blocks = (m - 1) * (n - 1)
        result[0] = total_blocks - sum(result[1:])
        
        return result

def countBlackBlocks(m: int, n: int, coordinates: List[List[int]]) -> List[int]:
    return Solution().countBlackBlocks(m, n, coordinates)