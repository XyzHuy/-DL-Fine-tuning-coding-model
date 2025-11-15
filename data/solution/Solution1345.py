import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque, defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        
        # Create a dictionary to hold indices of each value in arr
        value_to_indices = defaultdict(list)
        for i in range(n):
            value_to_indices[arr[i]].append(i)
        
        # BFS setup
        queue = deque([(0, 0)])  # (current_index, steps)
        visited = set([0])
        
        while queue:
            current_index, steps = queue.popleft()
            
            # Check if we've reached the last index
            if current_index == n - 1:
                return steps
            
            # Possible jumps
            for next_index in [current_index - 1, current_index + 1] + value_to_indices[arr[current_index]][::-1]:
                if 0 <= next_index < n and next_index not in visited:
                    visited.add(next_index)
                    queue.append((next_index, steps + 1))
            
            # Clear the list to prevent redundant checks in future iterations
            value_to_indices[arr[current_index]].clear()
        
        return -1  # This line should never be reached given the problem constraints

def minJumps(arr: List[int]) -> int:
    return Solution().minJumps(arr)