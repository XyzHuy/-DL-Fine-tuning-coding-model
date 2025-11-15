import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        # Build the graph
        graph = defaultdict(list)
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        # Set to keep track of unique nodes visited
        visited = set()
        visited.add(0)
        
        # Variable to store the maximum quality
        max_quality = 0
        
        def dfs(node, time_left, current_quality):
            nonlocal max_quality
            
            # If we return to node 0, update the maximum quality
            if node == 0:
                max_quality = max(max_quality, current_quality)
            
            # Explore neighbors
            for neighbor, time in graph[node]:
                if time_left >= time:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        dfs(neighbor, time_left - time, current_quality + values[neighbor])
                        visited.remove(neighbor)
                    else:
                        # If the neighbor is already visited, we can revisit it
                        dfs(neighbor, time_left - time, current_quality)
        
        # Start DFS from node 0
        dfs(0, maxTime, values[0])
        
        return max_quality

def maximalPathQuality(values: List[int], edges: List[List[int]], maxTime: int) -> int:
    return Solution().maximalPathQuality(values, edges, maxTime)