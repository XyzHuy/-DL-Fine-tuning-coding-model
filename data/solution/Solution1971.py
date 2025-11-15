import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # If the source is the same as the destination, return True
        if source == destination:
            return True
        
        # Build the adjacency list for the graph
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        # Initialize the queue for BFS and the visited set
        queue = deque([source])
        visited = set([source])
        
        # Perform BFS
        while queue:
            current = queue.popleft()
            
            # Check if we have reached the destination
            if current == destination:
                return True
            
            # Explore the neighbors of the current node
            for neighbor in adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        # If we exhaust the queue without finding the destination, return False
        return False

def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    return Solution().validPath(n, edges, source, destination)