import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create an adjacency list
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Initialize the distance array with infinity
        distances = [float('inf')] * (n + 1)
        distances[k] = 0
        
        # Priority queue to store (distance, node)
        priority_queue = [(0, k)]
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            # If the popped distance is greater than the recorded distance, skip it
            if current_distance > distances[current_node]:
                continue
            
            # Explore neighbors
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                
                # If a shorter path to the neighbor is found, update the distance and push to the queue
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        # Find the maximum distance in the distance array (excluding the 0th index)
        max_distance = max(distances[1:])
        
        # If the max distance is infinity, it means some nodes are unreachable
        return max_distance if max_distance != float('inf') else -1

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    return Solution().networkDelayTime(times, n, k)