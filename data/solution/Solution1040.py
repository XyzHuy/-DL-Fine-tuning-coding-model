import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        
        # Calculate the maximum number of moves
        max_moves = max(stones[n-1] - stones[1] - n + 2, stones[n-2] - stones[0] - n + 2)
        
        # Calculate the minimum number of moves
        min_moves = n
        i = 0
        for j in range(n):
            while stones[j] - stones[i] + 1 > n:
                i += 1
            inside = j - i + 1
            if inside == n - 1 and stones[j] - stones[i] + 1 == n - 1:
                min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, n - inside)
        
        return [min_moves, max_moves]

def numMovesStonesII(stones: List[int]) -> List[int]:
    return Solution().numMovesStonesII(stones)