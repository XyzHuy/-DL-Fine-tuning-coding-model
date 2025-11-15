import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # Initialize parent array for union-find
        parent = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}
        
        # Find function with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # Union function
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
        
        # Process all equality equations
        for equation in equations:
            if equation[1] == '=':
                union(equation[0], equation[3])
        
        # Process all inequality equations
        for equation in equations:
            if equation[1] == '!':
                if find(equation[0]) == find(equation[3]):
                    return False
        
        return True

def equationsPossible(equations: List[str]) -> bool:
    return Solution().equationsPossible(equations)