import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Build the graph as an adjacency list
        graph = defaultdict(list)
        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))
        
        # Max-heap with the initial node and probability 1 (as negative for max-heap)
        max_heap = [(-1.0, start_node)]
        probabilities = [0.0] * n
        probabilities[start_node] = 1.0
        
        while max_heap:
            current_prob, current_node = heapq.heappop(max_heap)
            
            # If we reached the end node, return the probability (negate it back)
            if current_node == end_node:
                return -current_prob
            
            # If the popped probability is less than the recorded one, skip
            if -current_prob < probabilities[current_node]:
                continue
            
            # Explore neighbors
            for neighbor, edge_prob in graph[current_node]:
                new_prob = -current_prob * edge_prob
                if new_prob > probabilities[neighbor]:
                    probabilities[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
        
        # If we exhaust the heap without reaching the end node, return 0
        return 0.0

def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
    return Solution().maxProbability(n, edges, succProb, start_node, end_node)