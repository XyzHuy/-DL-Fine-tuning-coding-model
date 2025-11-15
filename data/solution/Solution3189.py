import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        n = len(rooks)
        
        # Separate the row and column indices
        rows = [rook[0] for rook in rooks]
        cols = [rook[1] for rook in rooks]
        
        # Sort the row and column indices
        rows.sort()
        cols.sort()
        
        # Calculate the minimum number of moves
        moves = 0
        for i in range(n):
            moves += abs(rows[i] - i)  # Moves to place row rooks in correct positions
            moves += abs(cols[i] - i)  # Moves to place column rooks in correct positions
        
        return moves

# Example usage:
# sol = Solution()
# print(sol.minMoves([[0,0],[1,0],[1,1]]))  # Output: 3
# print(sol.minMoves([[0,0],[0,1],[0,2],[0,3]]))  # Output: 6

def minMoves(rooks: List[List[int]]) -> int:
    return Solution().minMoves(rooks)