import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Initialize the distance matrix with infinity
        dist = [[float('inf')] * 26 for _ in range(26)]
        
        # Set the distance for each transformation rule
        for src, dst, c in zip(original, changed, cost):
            src_idx = ord(src) - ord('a')
            dst_idx = ord(dst) - ord('a')
            dist[src_idx][dst_idx] = min(dist[src_idx][dst_idx], c)
        
        # Set the distance from each character to itself to 0
        for i in range(26):
            dist[i][i] = 0
        
        # Floyd-Warshall algorithm to find the shortest paths between all pairs of characters
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Calculate the total cost to convert source to target
        total_cost = 0
        for src, dst in zip(source, target):
            src_idx = ord(src) - ord('a')
            dst_idx = ord(dst) - ord('a')
            if dist[src_idx][dst_idx] == float('inf'):
                return -1
            total_cost += dist[src_idx][dst_idx]
        
        return total_cost

def minimumCost(source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
    return Solution().minimumCost(source, target, original, changed, cost)