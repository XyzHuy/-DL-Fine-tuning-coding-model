import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Build the graph with both directions
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1))  # Original direction with cost 1
            graph[v].append((u, 0))  # Reverse direction with cost 0

        def dfs(node, parent):
            cost = 0
            for neighbor, direction_cost in graph[node]:
                if neighbor == parent:
                    continue
                cost += direction_cost + dfs(neighbor, node)
            return cost

        # Start DFS from the capital city (0)
        return dfs(0, -1)

def minReorder(n: int, connections: List[List[int]]) -> int:
    return Solution().minReorder(n, connections)