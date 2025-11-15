import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict, deque
from typing import List

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize the queue for BFS: (current_time, current_node, number_of_visits)
        queue = deque([(0, 1, 0)])
        # Dictionary to keep track of the number of times each node has been visited
        visited = defaultdict(list)
        visited[1].append(0)
        
        while queue:
            current_time, current_node, visits = queue.popleft()
            
            # If we reach the node n for the second time, return the current_time
            if current_node == n and visits == 1:
                return current_time
            
            # Calculate the next time we can move (considering traffic lights)
            if (current_time // change) % 2 == 1:  # If the light is red
                next_time = (current_time // change + 1) * change
            else:  # If the light is green
                next_time = current_time
            
            # Explore neighbors
            for neighbor in graph[current_node]:
                # Calculate the time to reach the neighbor
                neighbor_time = next_time + time
                
                # If we have visited the neighbor less than 2 times, add to the queue
                if len(visited[neighbor]) < 2 and neighbor_time not in visited[neighbor]:
                    visited[neighbor].append(neighbor_time)
                    queue.append((neighbor_time, neighbor, len(visited[neighbor]) - 1))

def secondMinimum(n: int, edges: List[List[int]], time: int, change: int) -> int:
    return Solution().secondMinimum(n, edges, time, change)