import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict
from typing import List

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Step 1: Build the graph
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1
        
        # Step 2: Find the start node
        start = pairs[0][0]
        for node in graph:
            if out_degree[node] == in_degree[node] + 1:
                start = node
                break
        
        # Step 3: Use Hierholzer's algorithm to find the Eulerian path
        def dfs(node):
            while graph[node]:
                next_node = graph[node].pop()
                dfs(next_node)
                result.append([node, next_node])
        
        result = []
        dfs(start)
        
        # The result is in reverse order, so we need to reverse it
        return result[::-1]

def validArrangement(pairs: List[List[int]]) -> List[List[int]]:
    return Solution().validArrangement(pairs)