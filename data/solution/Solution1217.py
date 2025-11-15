import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # Count the number of chips at even and odd positions
        even_count = sum(1 for pos in position if pos % 2 == 0)
        odd_count = sum(1 for pos in position if pos % 2 != 0)
        
        # The minimum cost will be the smaller count because moving chips between even positions or odd positions is free
        return min(even_count, odd_count)

def minCostToMoveChips(position: List[int]) -> int:
    return Solution().minCostToMoveChips(position)