import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        # Directions for all possible lines: horizontal, vertical, and diagonal
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        # Try each direction
        for dr, dc in directions:
            r, c = rMove + dr, cMove + dc
            length = 1  # Start with the initial move cell
            
            # Move in the direction as long as we are within bounds and the cells are of the opposite color
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] != '.' and board[r][c] != color:
                r += dr
                c += dc
                length += 1
            
            # If we are still within bounds and the last cell is of our color and the line is at least 3 cells long
            if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == color and length >= 3:
                return True
        
        return False

def checkMove(board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
    return Solution().checkMove(board, rMove, cMove, color)