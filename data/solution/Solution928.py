import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque

class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        def bfs(start, banned_node):
            queue = deque([start])
            visited = set([start])
            while queue:
                node = queue.popleft()
                for neighbor in range(len(graph)):
                    if (graph[node][neighbor] == 1 and neighbor not in visited 
                        and neighbor != banned_node):
                        visited.add(neighbor)
                        queue.append(neighbor)
            return visited

        def spread(initial, banned_node):
            infected = set()
            for node in initial:
                if node == banned_node:
                    continue
                infected.update(bfs(node, banned_node))
            return len(infected)

        # Find the initial node whose removal minimizes the spread of malware
        min_infected = float('inf')
        best_node = min(initial)  # Default to the smallest index node if all have same impact
        for node in initial:
            infected_count = spread(initial, node)
            if infected_count < min_infected:
                min_infected = infected_count
                best_node = node
            elif infected_count == min_infected:
                best_node = min(best_node, node)
        
        return best_node

def minMalwareSpread(graph: List[List[int]], initial: List[int]) -> int:
    return Solution().minMalwareSpread(graph, initial)