import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        def dfs(node, dist, visited):
            if visited[node] != -1:
                # Cycle detected
                return dist - visited[node]
            if edges[node] == -1:
                # No outgoing edge
                return -1
            
            visited[node] = dist
            cycle_length = dfs(edges[node], dist + 1, visited)
            visited[node] = -1  # Backtrack to allow other cycles to use this node
            
            return cycle_length
        
        n = len(edges)
        visited = [-1] * n
        max_cycle = -1
        
        for i in range(n):
            if visited[i] == -1:
                max_cycle = max(max_cycle, dfs(i, 0, visited))
        
        return max_cycle

def longestCycle(edges: List[int]) -> int:
    return Solution().longestCycle(edges)