import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # Find the position of the rook
        rook_position = None
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook_position = (i, j)
                    break
            if rook_position:
                break
        
        # Directions for the rook to move: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        
        # Check each direction
        for dx, dy in directions:
            x, y = rook_position
            while 0 <= x + dx < 8 and 0 <= y + dy < 8:
                x += dx
                y += dy
                if board[x][y] == 'p':
                    count += 1
                    break
                elif board[x][y] != '.':
                    break
        
        return count

def numRookCaptures(board: List[List[str]]) -> int:
    return Solution().numRookCaptures(board)