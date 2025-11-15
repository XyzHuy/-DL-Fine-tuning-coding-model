import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Initialize the minimum number of recolors to a large number
        min_recolors = float('inf')
        
        # Iterate over each possible starting index for a block of length k
        for i in range(len(blocks) - k + 1):
            # Count the number of white blocks in the current window of length k
            white_count = blocks[i:i+k].count('W')
            # Update the minimum number of recolors needed
            min_recolors = min(min_recolors, white_count)
        
        return min_recolors

def minimumRecolors(blocks: str, k: int) -> int:
    return Solution().minimumRecolors(blocks, k)