import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            self.parent[rootU] = rootV

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)
        
        # Union all indices that can be swapped with each other
        for u, v in allowedSwaps:
            uf.union(u, v)
        
        # Group indices by their root in the union-find structure
        component_lists = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            component_lists[root].append(i)
        
        # Calculate the minimum Hamming distance
        min_hamming_distance = 0
        for indices in component_lists.values():
            src_count = defaultdict(int)
            tgt_count = defaultdict(int)
            for i in indices:
                src_count[source[i]] += 1
                tgt_count[target[i]] += 1
            
            # Calculate the mismatches for this component
            for num in src_count:
                min_hamming_distance += max(0, src_count[num] - tgt_count[num])
        
        return min_hamming_distance

def minimumHammingDistance(source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
    return Solution().minimumHammingDistance(source, target, allowedSwaps)