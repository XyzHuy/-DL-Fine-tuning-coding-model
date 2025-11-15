import random
import functools
import collections
import string
import math
import datetime


from collections import deque, defaultdict
from typing import List

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topologicalSort(vertices, edges):
            indegree = {i: 0 for i in vertices}
            adjacency_list = defaultdict(list)
            
            for u in edges:
                for v in edges[u]:
                    adjacency_list[u].append(v)
                    indegree[v] += 1
            
            queue = deque([v for v in vertices if indegree[v] == 0])
            result = []
            
            while queue:
                u = queue.popleft()
                result.append(u)
                
                for v in adjacency_list[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        queue.append(v)
            
            return result if len(result) == len(vertices) else []
        
        # Assign unique group ids to items without groups
        unique_id = m
        for u in range(n):
            if group[u] == -1:
                group[u] = unique_id
                unique_id += 1
        
        # Build graphs for groups and items within groups
        group_graph = defaultdict(set)
        item_graph = defaultdict(lambda: defaultdict(set))
        
        for v in range(n):
            for u in beforeItems[v]:
                if group[u] == group[v]:
                    item_graph[group[u]][u].add(v)
                else:
                    group_graph[group[u]].add(group[v])
        
        # Topological sort on groups
        group_order = topologicalSort(set(group), group_graph)
        if not group_order:
            return []
        
        # Topological sort on items within each group
        result = []
        for g in group_order:
            items_in_group = [u for u in range(n) if group[u] == g]
            item_order = topologicalSort(items_in_group, item_graph[g])
            if not item_order:
                return []
            result.extend(item_order)
        
        return result

def sortItems(n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
    return Solution().sortItems(n, m, group, beforeItems)