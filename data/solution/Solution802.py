import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        from collections import defaultdict
        
        n = len(graph)
        out_degree = [0] * n
        reverse_graph = defaultdict(list)
        
        # Build the reverse graph and compute out-degrees
        for i in range(n):
            for j in graph[i]:
                reverse_graph[j].append(i)
                out_degree[i] += 1
        
        # Queue for nodes with out-degree 0
        queue = deque([i for i in range(n) if out_degree[i] == 0])
        safe_nodes = set(queue)
        
        # Process the queue
        while queue:
            node = queue.popleft()
            for neighbor in reverse_graph[node]:
                out_degree[neighbor] -= 1
                if out_degree[neighbor] == 0:
                    queue.append(neighbor)
                    safe_nodes.add(neighbor)
        
        return sorted(safe_nodes)

def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
    return Solution().eventualSafeNodes(graph)