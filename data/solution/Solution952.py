import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.size = [1] * size
    
    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        # Union by rank
        if self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        elif self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        else:
            self.parent[rootQ] = rootP
            self.rank[rootP] += 1
            self.size[rootP] += self.size[rootQ]

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        max_num = max(nums)
        uf = UnionFind(max_num + 1)
        
        # Prime factorization and union
        prime_factor_to_index = defaultdict(int)
        for num in nums:
            original_num = num
            for factor in range(2, int(num ** 0.5) + 1):
                if num % factor == 0:
                    if factor not in prime_factor_to_index:
                        prime_factor_to_index[factor] = original_num
                    uf.union(original_num, prime_factor_to_index[factor])
                    while num % factor == 0:
                        num //= factor
            if num > 1:  # If num is a prime number greater than 1
                if num not in prime_factor_to_index:
                    prime_factor_to_index[num] = original_num
                uf.union(original_num, prime_factor_to_index[num])
        
        # Find the size of the largest component
        max_component_size = 0
        for num in nums:
            root = uf.find(num)
            max_component_size = max(max_component_size, uf.size[root])
        
        return max_component_size

def largestComponentSize(nums: List[int]) -> int:
    return Solution().largestComponentSize(nums)