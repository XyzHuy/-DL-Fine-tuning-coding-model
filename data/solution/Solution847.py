import random
import functools
import collections
import string
import math
import datetime


from collections import deque
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        
        # Initialize the queue with all nodes, each with their own bitmask
        queue = deque([(i, 1 << i, 0) for i in range(n)])
        # Initialize the visited set with all nodes' initial states
        visited = {(i, 1 << i) for i in range(n)}
        
        # Perform BFS
        while queue:
            current_node, visited_mask, path_length = queue.popleft()
            
            # Check if all nodes are visited
            if visited_mask == (1 << n) - 1:
                return path_length
            
            # Explore neighbors
            for neighbor in graph[current_node]:
                new_visited_mask = visited_mask | (1 << neighbor)
                if (neighbor, new_visited_mask) not in visited:
                    visited.add((neighbor, new_visited_mask))
                    queue.append((neighbor, new_visited_mask, path_length + 1))

def shortestPathLength(graph: List[List[int]]) -> int:
    return Solution().shortestPathLength(graph)