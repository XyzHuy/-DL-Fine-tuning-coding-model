import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        # Create an adjacency list to store the values of neighbors for each node
        neighbors = defaultdict(list)
        
        for a, b in edges:
            if vals[b] > 0:
                neighbors[a].append(vals[b])
            if vals[a] > 0:
                neighbors[b].append(vals[a])
        
        max_star_sum = float('-inf')
        
        for i in range(len(vals)):
            # Sort the neighbors in descending order
            neighbors[i].sort(reverse=True)
            # Calculate the star sum for the current node
            star_sum = vals[i] + sum(neighbors[i][:k])
            # Update the maximum star sum
            max_star_sum = max(max_star_sum, star_sum)
        
        return max_star_sum

def maxStarSum(vals: List[int], edges: List[List[int]], k: int) -> int:
    return Solution().maxStarSum(vals, edges, k)