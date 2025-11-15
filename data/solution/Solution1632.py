import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict
import itertools

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            self.parent[rootU] = rootV

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        # Create a map from value to a list of [row, col] pairs
        value_to_positions = defaultdict(list)
        for r in range(m):
            for c in range(n):
                value_to_positions[matrix[r][c]].append((r, c))
        
        # Initialize the rank matrix
        rank = [[0] * n for _ in range(m)]
        # Arrays to store the maximum rank in each row and column
        row_max_rank = [0] * m
        col_max_rank = [0] * n
        
        # Process each unique value in ascending order
        for value in sorted(value_to_positions):
            # Union-Find to group elements by their row or column
            uf = UnionFind(m + n)
            for r, c in value_to_positions[value]:
                uf.union(r, c + m)
            
            # Group the positions by their root in the union-find structure
            group = defaultdict(list)
            for r, c in value_to_positions[value]:
                root = uf.find(r)
                group[root].append((r, c))
            
            # Assign the rank to each group
            for positions in group.values():
                # Determine the max rank needed for this group
                max_rank = 0
                for r, c in positions:
                    max_rank = max(max_rank, row_max_rank[r], col_max_rank[c])
                
                # Assign the rank and update the row and column max ranks
                max_rank += 1
                for r, c in positions:
                    rank[r][c] = max_rank
                    row_max_rank[r] = max_rank
                    col_max_rank[c] = max_rank
        
        return rank

def matrixRankTransform(matrix: List[List[int]]) -> List[List[int]]:
    return Solution().matrixRankTransform(matrix)