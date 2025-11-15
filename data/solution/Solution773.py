import random
import functools
import collections
import string
import math
import datetime


from typing import List, Tuple
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Convert the 2x3 board to a tuple to use in a set
        start_state = tuple(tuple(row) for row in board)
        target_state = ((1, 2, 3), (4, 5, 0))
        
        # Possible moves for each position of 0 in the 2x3 board
        neighbors = {
            0: {1, 3},
            1: {0, 2, 4},
            2: {1, 5},
            3: {0, 4},
            4: {1, 3, 5},
            5: {2, 4}
        }
        
        # Find the initial position of 0
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    zero_pos = i * 3 + j
                    break
        
        # BFS initialization
        queue = deque([(start_state, zero_pos, 0)])  # (current_state, zero_position, moves)
        visited = set([start_state])
        
        while queue:
            current_state, zero_pos, moves = queue.popleft()
            
            # Check if the current state is the target state
            if current_state == target_state:
                return moves
            
            # Generate all possible next states
            for neighbor in neighbors[zero_pos]:
                new_state = [list(row) for row in current_state]  # Convert to list to modify
                new_zero_pos = neighbor
                i, j = divmod(zero_pos, 3)
                ni, nj = divmod(new_zero_pos, 3)
                
                # Swap the 0 with the neighbor
                new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
                new_state_tuple = tuple(tuple(row) for row in new_state)
                
                if new_state_tuple not in visited:
                    visited.add(new_state_tuple)
                    queue.append((new_state_tuple, new_zero_pos, moves + 1))
        
        # If we exhaust the queue without finding the target state, return -1
        return -1

def slidingPuzzle(board: List[List[int]]) -> int:
    return Solution().slidingPuzzle(board)