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
import heapq

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        max_heap = []
        unique_sums = set()

        def add_to_heap(val):
            if val not in unique_sums:
                unique_sums.add(val)
                heapq.heappush(max_heap, val)
                if len(max_heap) > 3:
                    unique_sums.remove(heapq.heappop(max_heap))

        # Check all possible rhombuses
        for i in range(m):
            for j in range(n):
                # Rhombus with area 0
                add_to_heap(grid[i][j])
                
                # Check larger rhombuses
                side_length = 1
                while True:
                    # Check if the current rhombus fits in the grid
                    if i - side_length < 0 or i + side_length >= m or j - side_length < 0 or j + side_length >= n:
                        break
                    
                    # Calculate the sum of the current rhombus
                    current_sum = 0
                    # Top to right
                    r, c = i - side_length, j
                    for _ in range(side_length):
                        current_sum += grid[r][c]
                        r += 1
                        c += 1
                    
                    # Right to bottom
                    for _ in range(side_length):
                        current_sum += grid[r][c]
                        r += 1
                        c -= 1
                    
                    # Bottom to left
                    for _ in range(side_length):
                        current_sum += grid[r][c]
                        r -= 1
                        c -= 1
                    
                    # Left to top
                    for _ in range(side_length):
                        current_sum += grid[r][c]
                        r -= 1
                        c += 1
                    
                    add_to_heap(current_sum)
                    side_length += 1

        return sorted(max_heap, reverse=True)

def getBiggestThree(grid: List[List[int]]) -> List[int]:
    return Solution().getBiggestThree(grid)