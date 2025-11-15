import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        # Build the graph as an adjacency list
        graph = [[] for _ in range(n)]
        for u, v, length in edges:
            graph[u].append((v, length))
            graph[v].append((u, length))
        
        # Priority queue for Dijkstra's algorithm
        pq = [(0, 0)]  # (current_time, current_node)
        # Array to store the minimum time to reach each node
        min_time = [float('inf')] * n
        min_time[0] = 0
        
        while pq:
            current_time, current_node = heapq.heappop(pq)
            
            # If we reach a node after it has disappeared, skip it
            if current_time >= disappear[current_node]:
                continue
            
            # Explore the neighbors
            for neighbor, length in graph[current_node]:
                new_time = current_time + length
                # If we can reach the neighbor before it disappears and in less time than previously recorded
                if new_time < disappear[neighbor] and new_time < min_time[neighbor]:
                    min_time[neighbor] = new_time
                    heapq.heappush(pq, (new_time, neighbor))
        
        # Convert the min_time array to the required answer format
        answer = [min_time[i] if min_time[i] != float('inf') else -1 for i in range(n)]
        return answer

def minimumTime(n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
    return Solution().minimumTime(n, edges, disappear)