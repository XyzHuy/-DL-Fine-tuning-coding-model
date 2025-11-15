import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Directions for the 8 neighbors
        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        rows = len(board)
        cols = len(board[0])
        
        # Use two bits to store the current state and the next state
        # Current state: cell >> 0 & 1 (least significant bit)
        # Next state: cell >> 1 & 1 (second least significant bit)
        
        # First pass: count live neighbors and mark next state
        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0
                
                # Count live neighbors
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (board[nr][nc] & 1) == 1:
                        live_neighbors += 1
                
                # Apply rules to determine the next state
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    # Live cell dies
                    board[r][c] = 1 | (0 << 1)  # 01 -> 01
                elif board[r][c] == 0 and live_neighbors == 3:
                    # Dead cell becomes live
                    board[r][c] = 0 | (1 << 1)  # 00 -> 10
                else:
                    # Cell remains in the same state
                    board[r][c] = board[r][c] | ((board[r][c] & 1) << 1)
        
        # Second pass: update the board to the next state
        for r in range(rows):
            for c in range(cols):
                board[r][c] >>= 1  # Shift right to get the next state

def gameOfLife(board: List[List[int]]) -> None:
    return Solution().gameOfLife(board)