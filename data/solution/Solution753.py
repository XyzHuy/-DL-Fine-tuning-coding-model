import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        # Initialize the Eulerian path with the starting node
        eulerian_path = []
        visited_edges = set()
        
        # Helper function to perform DFS and build the Eulerian path
        def dfs(node):
            for i in range(k):
                edge = node + str(i)
                if edge not in visited_edges:
                    visited_edges.add(edge)
                    dfs(edge[1:])
                    eulerian_path.append(str(i))
        
        # Start the DFS from the initial node of n-1 zeros
        start_node = '0' * (n - 1)
        dfs(start_node)
        
        # The Eulerian path will visit every edge exactly once
        # The final password is the Eulerian path + the start node (reversed)
        return ''.join(eulerian_path) + start_node

def crackSafe(n: int, k: int) -> str:
    return Solution().crackSafe(n, k)