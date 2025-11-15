import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Union-Find data structure with path compression and union by smallest element
        parent = {char: char for char in set(s1 + s2)}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            # Union by the smallest element
            if rootX != rootY:
                if rootX < rootY:
                    parent[rootY] = rootX
                else:
                    parent[rootX] = rootY

        # Create the equivalence classes
        for a, b in zip(s1, s2):
            union(a, b)

        # Build the smallest equivalent string
        result = []
        for char in baseStr:
            if char in parent:
                result.append(find(char))
            else:
                result.append(char)  # If the character is not in the equivalence classes, keep it as is

        return ''.join(result)

def smallestEquivalentString(s1: str, s2: str, baseStr: str) -> str:
    return Solution().smallestEquivalentString(s1, s2, baseStr)