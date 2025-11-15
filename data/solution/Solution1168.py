import random
import functools
import collections
import string
import math
import datetime


from typing import List
from heapq import heappop, heappush

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        # Add a virtual node (0) connected to each house with the cost of building a well
        for i in range(n):
            pipes.append([0, i + 1, wells[i]])
        
        # Sort all edges by cost
        pipes.sort(key=lambda x: x[2])
        
        # Union-Find data structure
        parent = list(range(n + 1))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX
                return True
            return False
        
        # Kruskal's algorithm to find the MST
        mst_cost = 0
        edges_used = 0
        for house1, house2, cost in pipes:
            if union(house1, house2):
                mst_cost += cost
                edges_used += 1
                if edges_used == n:
                    break
        
        return mst_cost

def minCostToSupplyWater(n: int, wells: List[int], pipes: List[List[int]]) -> int:
    return Solution().minCostToSupplyWater(n, wells, pipes)