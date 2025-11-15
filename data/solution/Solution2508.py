import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        # Create an adjacency list to represent the graph
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        # Find all nodes with odd degrees
        odd_degree_nodes = [node for node in range(1, n + 1) if len(graph[node]) % 2 != 0]
        
        # If there are no odd degree nodes, the graph is already valid
        if len(odd_degree_nodes) == 0:
            return True
        
        # If there are more than 4 odd degree nodes, it's impossible to fix with at most 2 edges
        if len(odd_degree_nodes) > 4:
            return False
        
        # If there are exactly 2 odd degree nodes, check if we can connect them directly
        if len(odd_degree_nodes) == 2:
            u, v = odd_degree_nodes
            if v not in graph[u]:
                return True
            else:
                # Try to find a third node that can connect to both u and v
                for w in range(1, n + 1):
                    if w not in graph[u] and w not in graph[v]:
                        return True
                return False
        
        # If there are exactly 4 odd degree nodes, try to pair them up
        if len(odd_degree_nodes) == 4:
            a, b, c, d = odd_degree_nodes
            # Check all possible pairings
            return (b not in graph[a] and d not in graph[c]) or \
                   (a not in graph[c] and d not in graph[b]) or \
                   (a not in graph[d] and c not in graph[b])
        
        # If there are 1 or 3 odd degree nodes, it's impossible to fix with at most 2 edges
        return False

def isPossible(n: int, edges: List[List[int]]) -> bool:
    return Solution().isPossible(n, edges)