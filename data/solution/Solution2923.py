import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # The champion team should have exactly n-1 wins (stronger than every other team)
        for i in range(n):
            if sum(grid[i]) == n - 1:
                return i

def findChampion(grid: List[List[int]]) -> int:
    return Solution().findChampion(grid)