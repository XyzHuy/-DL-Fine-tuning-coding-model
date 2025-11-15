import random
import functools
import collections
import string
import math
import datetime


from typing import List
from itertools import accumulate

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # Calculate the prefix sums of the stones array
        prefix_sums = list(accumulate(stones))
        
        # Initialize the maximum score difference
        max_diff = prefix_sums[-1]
        
        # Iterate from the end to the beginning to find the optimal move
        for i in range(len(prefix_sums) - 2, 0, -1):
            max_diff = max(max_diff, prefix_sums[i] - max_diff)
        
        return max_diff

def stoneGameVIII(stones: List[int]) -> int:
    return Solution().stoneGameVIII(stones)