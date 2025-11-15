import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_count = [0] * rows
        col_count = [0] * cols
        
        # Count servers in each row and column
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        # Count servers that can communicate
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    count += 1
        
        return count

def countServers(grid: List[List[int]]) -> int:
    return Solution().countServers(grid)