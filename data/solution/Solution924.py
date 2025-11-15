import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        def dfs(node, component_id):
            if visited[node]:
                return
            visited[node] = True
            component[node] = component_id
            component_size[component_id] += 1
            for neighbor in range(len(graph)):
                if graph[node][neighbor] == 1:
                    dfs(neighbor, component_id)

        n = len(graph)
        visited = [False] * n
        component = [-1] * n
        component_size = {}
        component_id = 0

        # Identify connected components
        for node in range(n):
            if not visited[node]:
                component_size[component_id] = 0
                dfs(node, component_id)
                component_id += 1

        # Count how many initial infected nodes belong to each component
        infected_count = [0] * component_id
        for node in initial:
            infected_count[component[node]] += 1

        # Find the node to remove
        max_infected_saved = 0
        best_node = min(initial)

        for node in initial:
            comp = component[node]
            if infected_count[comp] == 1:  # Only consider components with exactly one infected node
                if component_size[comp] > max_infected_saved:
                    max_infected_saved = component_size[comp]
                    best_node = node
                elif component_size[comp] == max_infected_saved:
                    best_node = min(best_node, node)

        return best_node

def minMalwareSpread(graph: List[List[int]], initial: List[int]) -> int:
    return Solution().minMalwareSpread(graph, initial)