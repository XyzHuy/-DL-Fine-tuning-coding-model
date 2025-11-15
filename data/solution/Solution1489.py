import random
import functools
import collections
import string
import math
import datetime


class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.n = n

    def union(self, a, b):
        if self.find(a) == self.find(b):
            return False
        self.p[self.find(a)] = self.find(b)
        self.n -= 1
        return True

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i)
        edges.sort(key=lambda x: x[2])
        uf = UnionFind(n)
        mst_weight = sum(w for f, t, w, _ in edges if uf.union(f, t))
        critical_edges = []
        pseudo_critical_edges = []

        for f, t, w, i in edges:
            # Check if edge is critical
            uf = UnionFind(n)
            mst_without_edge = sum(z for x, y, z, j in edges if j != i and uf.union(x, y))
            if uf.n > 1 or mst_without_edge > mst_weight:
                critical_edges.append(i)
                continue

            # Check if edge is pseudo-critical
            uf = UnionFind(n)
            uf.union(f, t)
            mst_with_edge = w + sum(z for x, y, z, j in edges if j != i and uf.union(x, y))
            if mst_with_edge == mst_weight:
                pseudo_critical_edges.append(i)

        return [critical_edges, pseudo_critical_edges]

def findCriticalAndPseudoCriticalEdges(n: int, edges: List[List[int]]) -> List[List[int]]:
    return Solution().findCriticalAndPseudoCriticalEdges(n, edges)