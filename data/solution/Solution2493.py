import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict, deque
from typing import List

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Find all connected components
        visited = [False] * (n + 1)
        components = []
        
        def dfs(node, component):
            stack = [node]
            while stack:
                current = stack.pop()
                if not visited[current]:
                    visited[current] = True
                    component.append(current)
                    for neighbor in graph[current]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
        
        for node in range(1, n + 1):
            if not visited[node]:
                component = []
                dfs(node, component)
                components.append(component)
        
        # Step 3: Check bipartiteness and calculate the maximum number of groups
        def is_bipartite(component):
            color = [0] * (n + 1)  # 0: uncolored, 1: color1, -1: color2
            for node in component:
                if color[node] == 0:
                    queue = deque([node])
                    color[node] = 1
                    while queue:
                        current = queue.popleft()
                        for neighbor in graph[current]:
                            if color[neighbor] == color[current]:
                                return False
                            if color[neighbor] == 0:
                                color[neighbor] = -color[current]
                                queue.append(neighbor)
            return True
        
        def max_groups(component):
            max_groups = 0
            for start in component:
                queue = deque([(start, 1)])  # (node, group number)
                visited = set()
                visited.add(start)
                current_groups = 0
                while queue:
                    current, group = queue.popleft()
                    current_groups = group
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append((neighbor, group + 1))
                max_groups = max(max_groups, current_groups)
            return max_groups
        
        total_groups = 0
        for component in components:
            if not is_bipartite(component):
                return -1
            total_groups += max_groups(component)
        
        return total_groups

def magnificentSets(n: int, edges: List[List[int]]) -> int:
    return Solution().magnificentSets(n, edges)