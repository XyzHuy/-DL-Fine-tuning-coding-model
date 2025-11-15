import random
import functools
import collections
import string
import math
import datetime


from functools import cache
from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            return max(piles[i] - dfs(i + 1, j), piles[j] - dfs(i, j - 1))

        return dfs(0, len(piles) - 1) > 0

def stoneGame(piles: List[int]) -> bool:
    return Solution().stoneGame(piles)