import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
        return True

mx = 100010
p = defaultdict(list)
for x in range(1, mx + 1):
    v = x
    i = 2
    while i <= v // i:
        if v % i == 0:
            p[x].append(i)
            while v % i == 0:
                v //= i
        i += 1
    if v > 1:
        p[x].append(v)

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if 1 in nums:
            return False
        
        n = len(nums)
        m = max(nums)
        uf = UnionFind(n + m + 1)
        
        for i, x in enumerate(nums):
            for j in p[x]:
                uf.union(i, j + n)
        
        # Check if all elements are in the same connected component
        root = uf.find(0)
        for i in range(1, n):
            if uf.find(i) != root:
                return False
        
        return True

def canTraverseAllPairs(nums: List[int]) -> bool:
    return Solution().canTraverseAllPairs(nums)