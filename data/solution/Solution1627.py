import random
import functools
import collections
import string
import math
import datetime


from typing import List

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return False
        if self.rank[rootQ] > self.rank[rootP]:
            rootP, rootQ = rootQ, rootP
        self.parent[rootQ] = rootP
        if self.rank[rootP] == self.rank[rootQ]:
            self.rank[rootP] += 1
        return True

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        if threshold == 0:
            return [True] * len(queries)
        
        uf = UnionFind(n + 1)
        
        for i in range(threshold + 1, n + 1):
            for j in range(2 * i, n + 1, i):
                uf.union(i, j)
        
        return [uf.find(a) == uf.find(b) for a, b in queries]

def areConnected(n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
    return Solution().areConnected(n, threshold, queries)