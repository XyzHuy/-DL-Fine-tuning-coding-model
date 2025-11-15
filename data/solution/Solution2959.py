import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict
import heapq
from itertools import combinations

class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        def shortest_paths(graph, source, num_nodes):
            distances = [float('inf')] * num_nodes
            distances[source] = 0
            pq = [(0, source)]
            while pq:
                dist, node = heapq.heappop(pq)
                if dist > distances[node]:
                    continue
                for neighbor, weight in graph[node]:
                    if dist + weight < distances[neighbor]:
                        distances[neighbor] = dist + weight
                        heapq.heappush(pq, (dist + weight, neighbor))
            return distances

        def is_valid_subset(subset):
            # Build the graph for the current subset of branches
            graph = defaultdict(list)
            for u, v, w in roads:
                if u in subset and v in subset:
                    graph[u].append((v, w))
                    graph[v].append((u, w))
            
            # Check the distance between all pairs of nodes in the subset
            for node in subset:
                distances = shortest_paths(graph, node, n)
                for other_node in subset:
                    if other_node != node and distances[other_node] > maxDistance:
                        return False
            return True

        count = 0
        # Check all subsets of branches
        for r in range(n + 1):
            for subset in combinations(range(n), r):
                if is_valid_subset(subset):
                    count += 1
        return count

def numberOfSets(n: int, maxDistance: int, roads: List[List[int]]) -> int:
    return Solution().numberOfSets(n, maxDistance, roads)