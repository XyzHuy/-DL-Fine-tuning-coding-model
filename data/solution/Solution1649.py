import random
import functools
import collections
import string
import math
import datetime


from typing import List

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, idx, delta):
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & -idx
    
    def query(self, idx):
        sum = 0
        while idx > 0:
            sum += self.tree[idx]
            idx -= idx & -idx
        return sum

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(instructions)
        fenwick_tree = FenwickTree(max_val)
        
        total_cost = 0
        for i, num in enumerate(instructions):
            # Count of elements strictly less than num
            count_less = fenwick_tree.query(num - 1)
            # Count of elements strictly greater than num
            count_greater = i - fenwick_tree.query(num)
            
            # Cost is the minimum of count_less and count_greater
            cost = min(count_less, count_greater)
            total_cost = (total_cost + cost) % MOD
            
            # Update the Fenwick Tree with the current number
            fenwick_tree.update(num, 1)
        
        return total_cost

def createSortedArray(instructions: List[int]) -> int:
    return Solution().createSortedArray(instructions)