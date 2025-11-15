import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        def flip(matrix, x, y):
            directions = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    matrix[nx][ny] ^= 1

        def matrix_to_tuple(matrix):
            return tuple(tuple(row) for row in matrix)

        m, n = len(mat), len(mat[0])
        start = matrix_to_tuple(mat)
        target = tuple(tuple(0 for _ in range(n)) for _ in range(m))
        
        if start == target:
            return 0

        queue = deque([(start, 0)])
        visited = set([start])

        while queue:
            current_matrix, steps = queue.popleft()

            for i in range(m):
                for j in range(n):
                    new_matrix = [list(row) for row in current_matrix]
                    flip(new_matrix, i, j)
                    new_tuple = matrix_to_tuple(new_matrix)

                    if new_tuple == target:
                        return steps + 1

                    if new_tuple not in visited:
                        visited.add(new_tuple)
                        queue.append((new_tuple, steps + 1))

        return -1

def minFlips(mat: List[List[int]]) -> int:
    return Solution().minFlips(mat)