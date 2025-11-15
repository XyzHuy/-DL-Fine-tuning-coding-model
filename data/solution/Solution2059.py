import random
import functools
import collections
import string
import math
import datetime


from collections import deque
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        # Initialize the queue with the starting value and 0 operations
        queue = deque([(start, 0)])
        # Set to keep track of visited values
        visited = set([start])
        
        while queue:
            current, ops = queue.popleft()
            
            # Try all possible operations with each number in nums
            for num in nums:
                for next_val in [current + num, current - num, current ^ num]:
                    # Check if we have reached the goal
                    if next_val == goal:
                        return ops + 1
                    # If the next value is within the valid range and not visited, add to queue
                    if 0 <= next_val <= 1000 and next_val not in visited:
                        visited.add(next_val)
                        queue.append((next_val, ops + 1))
        
        # If we exhaust the queue without finding the goal, return -1
        return -1

def minimumOperations(nums: List[int], start: int, goal: int) -> int:
    return Solution().minimumOperations(nums, start, goal)