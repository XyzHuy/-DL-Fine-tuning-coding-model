import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        from collections import defaultdict
        
        # Build the graph
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        # Cache to store the reachability information
        cache = {}
        
        def dfs(node, target):
            if (node, target) in cache:
                return cache[(node, target)]
            if node == target:
                return True
            for neighbor in graph[node]:
                if dfs(neighbor, target):
                    cache[(node, neighbor)] = True
                    cache[(node, target)] = True
                    return True
            cache[(node, target)] = False
            return False
        
        # Process each query
        result = []
        for u, v in queries:
            result.append(dfs(u, v))
        
        return result

def checkIfPrerequisite(numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    return Solution().checkIfPrerequisite(numCourses, prerequisites, queries)