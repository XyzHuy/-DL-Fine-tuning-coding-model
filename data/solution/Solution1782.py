import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict
from typing import List

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        # Step 1: Count the degree of each node
        degree = [0] * (n + 1)
        overlap = defaultdict(int)
        
        for u, v in edges:
            if u > v:
                u, v = v, u
            degree[u] += 1
            degree[v] += 1
            overlap[(u, v)] += 1
        
        # Step 2: Sort the degrees
        sorted_degree = sorted(degree)
        
        # Step 3: Prepare the answer for each query
        answers = []
        
        for query in queries:
            # Step 4: Two-pointer technique to count valid pairs
            count = 0
            left, right = 1, n
            
            while left < right:
                if sorted_degree[left] + sorted_degree[right] > query:
                    count += right - left
                    right -= 1
                else:
                    left += 1
            
            # Step 5: Adjust for overlaps
            for (u, v), cnt in overlap.items():
                if degree[u] + degree[v] > query and degree[u] + degree[v] - cnt <= query:
                    count -= 1
            
            answers.append(count)
        
        return answers

def countPairs(n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
    return Solution().countPairs(n, edges, queries)