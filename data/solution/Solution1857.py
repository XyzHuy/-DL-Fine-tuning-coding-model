import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict, deque

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n
        
        # Build the graph and calculate indegrees
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        # Initialize the DP table
        dp = [[0] * 26 for _ in range(n)]
        
        # Queue for topological sorting
        queue = deque([i for i in range(n) if indegree[i] == 0])
        processed_nodes = 0
        
        # Process nodes in topological order
        while queue:
            node = queue.popleft()
            processed_nodes += 1
            color_index = ord(colors[node]) - ord('a')
            dp[node][color_index] += 1
            
            for neighbor in graph[node]:
                for c in range(26):
                    dp[neighbor][c] = max(dp[neighbor][c], dp[node][c])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If we didn't process all nodes, there's a cycle
        if processed_nodes != n:
            return -1
        
        # Find the maximum color value
        return max(max(row) for row in dp)

def largestPathValue(colors: str, edges: List[List[int]]) -> int:
    return Solution().largestPathValue(colors, edges)