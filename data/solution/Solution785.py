import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n  # 0 means uncolored, 1 and -1 are the two colors

        def dfs(node, c):
            if color[node] != 0:
                return color[node] == c
            color[node] = c
            for neighbor in graph[node]:
                if not dfs(neighbor, -c):
                    return False
            return True

        for i in range(n):
            if color[i] == 0:  # If the node is not colored
                if not dfs(i, 1):  # Try to color it with color 1
                    return False
        return True

def isBipartite(graph: List[List[int]]) -> bool:
    return Solution().isBipartite(graph)