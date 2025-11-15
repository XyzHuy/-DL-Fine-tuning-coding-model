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
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        # Create adjacency lists for the original graph and its reverse
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        
        for u, v, weight in edges:
            graph[u].append((v, weight))
            reverse_graph[v].append((u, weight))
        
        # Dijkstra's algorithm to find shortest paths
        def dijkstra(graph, start):
            distances = [float('inf')] * n
            distances[start] = 0
            priority_queue = [(0, start)]
            
            while priority_queue:
                current_distance, current_node = heapq.heappop(priority_queue)
                
                if current_distance > distances[current_node]:
                    continue
                
                for neighbor, weight in graph[current_node]:
                    distance = current_distance + weight
                    
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(priority_queue, (distance, neighbor))
            
            return distances
        
        # Compute shortest paths from src1, src2, and dest (in the reversed graph)
        dist_from_src1 = dijkstra(graph, src1)
        dist_from_src2 = dijkstra(graph, src2)
        dist_to_dest = dijkstra(reverse_graph, dest)
        
        # Find the minimum weight of the subgraph
        min_weight = float('inf')
        for i in range(n):
            total_weight = dist_from_src1[i] + dist_from_src2[i] + dist_to_dest[i]
            if total_weight < min_weight:
                min_weight = total_weight
        
        return min_weight if min_weight < float('inf') else -1

def minimumWeight(n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
    return Solution().minimumWeight(n, edges, src1, src2, dest)