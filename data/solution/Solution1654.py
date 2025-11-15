import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        # Convert forbidden list to a set for O(1) lookups
        forbidden_set = set(forbidden)
        # Define a set to keep track of visited states (position, last_jump_direction)
        visited = set()
        # We start at position 0, with no previous jump (None for direction)
        queue = deque([(0, None, 0)])  # (position, last_jump_direction, number_of_jumps)
        # Define the maximum position to explore
        max_position = 4000  # This is an upper bound based on the problem constraints
        
        while queue:
            position, last_jump, jumps = queue.popleft()
            
            # If we reach the target position, return the number of jumps
            if position == x:
                return jumps
            
            # Calculate the next forward jump position
            next_forward = position + a
            # Check if the forward jump is within bounds, not forbidden, and not visited
            if next_forward <= max_position and next_forward not in forbidden_set and (next_forward, 'forward') not in visited:
                visited.add((next_forward, 'forward'))
                queue.append((next_forward, 'forward', jumps + 1))
            
            # Calculate the next backward jump position
            next_backward = position - b
            # Check if the backward jump is within bounds, not forbidden, and not visited
            # Also, ensure we haven't just jumped backward in the previous move
            if next_backward >= 0 and next_backward not in forbidden_set and (next_backward, 'backward') not in visited and last_jump != 'backward':
                visited.add((next_backward, 'backward'))
                queue.append((next_backward, 'backward', jumps + 1))
        
        # If we exhaust the queue without finding a path to x, return -1
        return -1

def minimumJumps(forbidden: List[int], a: int, b: int, x: int) -> int:
    return Solution().minimumJumps(forbidden, a, b, x)