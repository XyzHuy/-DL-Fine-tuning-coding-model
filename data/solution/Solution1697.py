import random
import functools
import collections
import string
import math
import datetime


from typing import List
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Helper function to find the root of a node with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # Helper function to union two sets
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
        
        # Initialize Union-Find data structure
        parent = list(range(n))
        rank = [0] * n
        
        # Sort edges by distance
        edgeList.sort(key=lambda x: x[2])
        
        # Sort queries by limit, keeping track of original indices
        indexedQueries = sorted(enumerate(queries), key=lambda x: x[1][2])
        
        # Result array to store answers for each query
        result = [False] * len(queries)
        
        # Index to keep track of where we are in the edgeList
        edgeIndex = 0
        
        # Process each query in sorted order
        for queryIndex, (p, q, limit) in indexedQueries:
            # Add all edges with distance < limit to the Union-Find structure
            while edgeIndex < len(edgeList) and edgeList[edgeIndex][2] < limit:
                u, v, _ = edgeList[edgeIndex]
                union(u, v)
                edgeIndex += 1
            
            # Check if p and q are connected
            if find(p) == find(q):
                result[queryIndex] = True
        
        return result

def distanceLimitedPathsExist(n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
    return Solution().distanceLimitedPathsExist(n, edgeList, queries)