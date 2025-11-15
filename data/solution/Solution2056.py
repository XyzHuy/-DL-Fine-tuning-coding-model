import random
import functools
import collections
import string
import math
import datetime


from typing import List
from itertools import product

class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        def get_moves(piece, r, c):
            directions = []
            if piece == "rook" or piece == "queen":
                directions.extend([(1, 0), (-1, 0), (0, 1), (0, -1)])
            if piece == "bishop" or piece == "queen":
                directions.extend([(1, 1), (1, -1), (-1, 1), (-1, -1)])
            
            moves = []
            for dr, dc in directions:
                for step in range(1, 8):
                    nr, nc = r + dr * step, c + dc * step
                    if 1 <= nr <= 8 and 1 <= nc <= 8:
                        moves.append((nr, nc))
            moves.append((r, c))  # Option to stay in the same place
            return moves

        def is_valid_combination(combination):
            n = len(combination)
            pos = [tuple(p) for p in positions]
            visited = [set([pos[i]]) for i in range(n)]
            max_time = max(max(abs(combination[i][0] - positions[i][0]), abs(combination[i][1] - positions[i][1])) for i in range(n))
            
            for t in range(1, max_time + 1):
                next_pos = []
                for i in range(n):
                    r, c = pos[i]
                    tr, tc = combination[i]
                    if tr == r and tc == c:
                        next_pos.append((r, c))
                    else:
                        if tr > r:
                            r += 1
                        elif tr < r:
                            r -= 1
                        if tc > c:
                            c += 1
                        elif tc < c:
                            c -= 1
                        next_pos.append((r, c))
                if len(set(next_pos)) != n:
                    return False
                for i in range(n):
                    visited[i].add(next_pos[i])
                pos = next_pos
            return True

        all_moves = [get_moves(p, r, c) for p, (r, c) in zip(pieces, positions)]
        valid_combinations = 0

        for combination in product(*all_moves):
            if is_valid_combination(combination):
                valid_combinations += 1

        return valid_combinations

def countCombinations(pieces: List[str], positions: List[List[int]]) -> int:
    return Solution().countCombinations(pieces, positions)