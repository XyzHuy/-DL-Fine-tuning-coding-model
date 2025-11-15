import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        # Sort the positions to ensure x < y < z
        x, y, z = sorted([a, b, c])
        
        # Calculate the gaps between the stones
        gap1 = y - x
        gap2 = z - y
        
        # Determine the minimum number of moves
        if gap1 == 1 and gap2 == 1:
            min_moves = 0
        elif gap1 <= 2 or gap2 <= 2:
            min_moves = 1
        else:
            min_moves = 2
        
        # The maximum number of moves is the sum of the gaps minus 2
        max_moves = gap1 + gap2 - 2
        
        return [min_moves, max_moves]

def numMovesStones(a: int, b: int, c: int) -> List[int]:
    return Solution().numMovesStones(a, b, c)