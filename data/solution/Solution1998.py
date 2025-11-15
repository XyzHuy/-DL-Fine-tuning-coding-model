import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict
from math import gcd

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        if nums == sorted(nums):
            return True
        
        max_num = max(nums)
        uf = UnionFind(max_num + 1)
        
        # Factorize each number and union the number with its prime factors
        def prime_factors(n):
            factor = 2
            while factor * factor <= n:
                while n % factor == 0:
                    yield factor
                    n //= factor
                factor += 1
            if n > 1:
                yield n
        
        for num in nums:
            factors = list(prime_factors(num))
            for factor in factors:
                uf.union(num, factor)
        
        # Create a mapping from each number to its root component
        num_to_root = {num: uf.find(num) for num in nums}
        
        # Create a sorted version of nums
        sorted_nums = sorted(nums)
        
        # Check if we can sort nums by swapping within components
        for original, sorted_num in zip(nums, sorted_nums):
            if num_to_root[original] != num_to_root[sorted_num]:
                return False
        
        return True

def gcdSort(nums: List[int]) -> bool:
    return Solution().gcdSort(nums)