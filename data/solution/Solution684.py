import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX  # Union by rank can be added for optimization
                return True
            return False
        
        for x, y in edges:
            if x not in parent:
                parent[x] = x
            if y not in parent:
                parent[y] = y
            if not union(x, y):
                return [x, y]
        
        return []

def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    return Solution().findRedundantConnection(edges)