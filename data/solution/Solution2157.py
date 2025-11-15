import random
import functools
import collections
import string
import math
import datetime


from typing import List, DefaultDict
from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.size = [1] * size
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        elif self.rank[pv] > self.rank[pu]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1
            self.size[pv] += self.size[pu]

class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        def get_mask(word):
            mask = 0
            for char in word:
                mask |= (1 << (ord(char) - ord('a')))
            return mask
        
        n = len(words)
        uf = UnionFind(n)
        mask_to_indices = defaultdict(list)
        
        for i, word in enumerate(words):
            mask = get_mask(word)
            if mask in mask_to_indices:
                for j in mask_to_indices[mask]:
                    uf.union(i, j)
            mask_to_indices[mask].append(i)
            
        # Check for connections by adding/deleting a single letter
        for i, word in enumerate(words):
            mask = get_mask(word)
            for char in word:
                bit = (1 << (ord(char) - ord('a')))
                new_mask = mask ^ bit
                if new_mask in mask_to_indices:
                    for j in mask_to_indices[new_mask]:
                        uf.union(i, j)
            
            # Check for connections by replacing a single letter
            for char in word:
                bit = (1 << (ord(char) - ord('a')))
                base_mask = mask ^ bit
                for new_char in 'abcdefghijklmnopqrstuvwxyz':
                    if new_char != char:
                        new_bit = (1 << (ord(new_char) - ord('a')))
                        new_mask = base_mask | new_bit
                        if new_mask in mask_to_indices:
                            for j in mask_to_indices[new_mask]:
                                uf.union(i, j)
        
        max_group_size = 0
        unique_groups = set()
        for i in range(n):
            root = uf.find(i)
            unique_groups.add(root)
            max_group_size = max(max_group_size, uf.size[root])
        
        return [len(unique_groups), max_group_size]

def groupStrings(words: List[str]) -> List[int]:
    return Solution().groupStrings(words)