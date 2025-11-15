import random
import functools
import collections
import string
import math
import datetime


from collections import deque, defaultdict
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def bfs(s: int):
            q = deque([s])
            vis = {s}
            while q:
                i = q.popleft()
                for j in g[i]:
                    if j not in vis:
                        vis.add(j)
                        q.append(j)
                        ans[j].add(s)

        # Create the adjacency list for the graph
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
        
        # Initialize the answer list with sets to avoid duplicates
        ans = [set() for _ in range(n)]
        
        # Perform BFS for each node to find all its ancestors
        for i in range(n):
            bfs(i)
        
        # Convert sets to sorted lists
        return [sorted(list(ancestors)) for ancestors in ans]

def getAncestors(n: int, edges: List[List[int]]) -> List[List[int]]:
    return Solution().getAncestors(n, edges)