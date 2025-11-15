import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        # Union-Find data structure
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
        
        # Convert restrictions to a dictionary for quick lookup
        restricted = {}
        for x, y in restrictions:
            if x not in restricted:
                restricted[x] = set()
            if y not in restricted:
                restricted[y] = set()
            restricted[x].add(y)
            restricted[y].add(x)
        
        result = []
        
        for u, v in requests:
            rootU = find(u)
            rootV = find(v)
            
            # Check if the request is valid
            valid = True
            for x in range(n):
                rootX = find(x)
                if rootX in [rootU, rootV]:
                    if x in restricted:
                        for y in restricted[x]:
                            rootY = find(y)
                            if rootY in [rootU, rootV]:
                                valid = False
                                break
                if not valid:
                    break
            
            if valid:
                union(u, v)
            
            result.append(valid)
        
        return result

def friendRequests(n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
    return Solution().friendRequests(n, restrictions, requests)