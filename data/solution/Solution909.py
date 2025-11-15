import random
import functools
import collections
import string
import math
import datetime


from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        
        # Function to convert square number to board coordinates
        def get_board_position(square):
            quot, rem = divmod(square - 1, n)
            row = n - 1 - quot
            col = rem if quot % 2 == 0 else n - 1 - rem
            return row, col
        
        # BFS initialization
        queue = deque([(1, 0)])  # (current square, number of moves)
        visited = set()
        
        while queue:
            current, moves = queue.popleft()
            
            if current == target:
                return moves
            
            for i in range(1, 7):  # Roll the die
                next_square = current + i
                if next_square > target:
                    break
                
                if next_square not in visited:
                    visited.add(next_square)
                    row, col = get_board_position(next_square)
                    if board[row][col] != -1:  # There's a snake or ladder
                        next_square = board[row][col]
                    
                    queue.append((next_square, moves + 1))
        
        return -1  # If we exhaust the queue without reaching the target

def snakesAndLadders(board: List[List[int]]) -> int:
    return Solution().snakesAndLadders(board)