import random
import functools
import collections
import string
import math
import datetime


from collections import deque
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # Create adjacency lists for red and blue edges
        red_adj = [[] for _ in range(n)]
        blue_adj = [[] for _ in range(n)]
        
        for u, v in redEdges:
            red_adj[u].append(v)
        for u, v in blueEdges:
            blue_adj[u].append(v)
        
        # Initialize the answer array with infinity
        answer = [[float('inf'), float('inf')] for _ in range(n)]
        answer[0] = [0, 0]  # Starting point, 0 distance for both colors
        
        # Queue for BFS: (node, last_color_used)
        # 0 for red, 1 for blue
        queue = deque([(0, 0), (0, 1)])
        
        while queue:
            node, last_color = queue.popleft()
            next_color = 1 - last_color  # Alternate color
            adj = blue_adj if last_color == 0 else red_adj
            
            for neighbor in adj[node]:
                if answer[neighbor][next_color] == float('inf'):
                    answer[neighbor][next_color] = answer[node][last_color] + 1
                    queue.append((neighbor, next_color))
        
        # Prepare the result array
        result = [min(answer[i]) for i in range(n)]
        return [-1 if x == float('inf') else x for x in result]

def shortestAlternatingPaths(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    return Solution().shortestAlternatingPaths(n, redEdges, blueEdges)