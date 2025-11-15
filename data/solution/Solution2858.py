import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        # Build the graph with edge direction information
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append((v, 0))  # 0 means the edge is original
            graph[v].append((u, 1))  # 1 means the edge is reversed
        
        # Helper function to calculate the number of reversals needed
        def dfs(u, parent):
            count = 0
            for v, rev in graph[u]:
                if v == parent:
                    continue
                count += dfs(v, u) + rev
            return count
        
        # Calculate the number of reversals needed for node 0
        answer = [0] * n
        answer[0] = dfs(0, -1)
        
        # Use the answer for node 0 to calculate answers for other nodes
        def dfs2(u, parent):
            for v, rev in graph[u]:
                if v == parent:
                    continue
                answer[v] = answer[u] + 1 - 2 * rev  # Adjust the count for the child node
                dfs2(v, u)
        
        dfs2(0, -1)
        return answer

def minEdgeReversals(n: int, edges: List[List[int]]) -> List[int]:
    return Solution().minEdgeReversals(n, edges)