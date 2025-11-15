import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Create a graph using adjacency list
        graph = [[] for _ in range(n + 1)]
        for a, b, distance in roads:
            graph[a].append((b, distance))
            graph[b].append((a, distance))
        
        # Initialize the minimum score to a large value
        min_score = float('inf')
        
        # Use a set to keep track of visited cities
        visited = set()
        
        # Define a recursive DFS function to explore the graph
        def dfs(city):
            nonlocal min_score
            if city in visited:
                return
            visited.add(city)
            for neighbor, distance in graph[city]:
                min_score = min(min_score, distance)
                dfs(neighbor)
        
        # Start DFS from city 1
        dfs(1)
        
        return min_score

def minScore(n: int, roads: List[List[int]]) -> int:
    return Solution().minScore(n, roads)