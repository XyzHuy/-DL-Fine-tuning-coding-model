import random
import functools
import collections
import string
import math
import datetime


from collections import deque

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        # Initialize the queue with the starting value and operation count
        queue = deque([(x, 0)])
        # Set to keep track of visited states
        visited = set([x])
        
        while queue:
            current, ops = queue.popleft()
            
            # If we have reached the target value, return the number of operations
            if current == y:
                return ops
            
            # Generate the next states
            next_states = [
                (current - 1, ops + 1),  # Decrement by 1
                (current + 1, ops + 1),  # Increment by 1
            ]
            
            if current % 11 == 0:
                next_states.append((current // 11, ops + 1))  # Divide by 11
            if current % 5 == 0:
                next_states.append((current // 5, ops + 1))   # Divide by 5
            
            # Enqueue the next states if they haven't been visited
            for next_state, next_ops in next_states:
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, next_ops))
        
        # If we exhaust the queue without finding y, return -1 (should not happen with valid input)
        return -1

# Example usage:
sol = Solution()
print(sol.minimumOperationsToMakeEqual(26, 1))  # Output: 3
print(sol.minimumOperationsToMakeEqual(54, 2))  # Output: 4
print(sol.minimumOperationsToMakeEqual(25, 30)) # Output: 5

def minimumOperationsToMakeEqual(x: int, y: int) -> int:
    return Solution().minimumOperationsToMakeEqual(x, y)