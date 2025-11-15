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
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        # Build the graph
        graph = defaultdict(list)
        for a, b, cost in roads:
            graph[a].append((b, cost))
            graph[b].append((a, cost))
        
        def dijkstra(start):
            # Priority queue for Dijkstra's algorithm
            pq = [(0, start)]
            # Distance array to store the minimum distance from start to each node
            dist = [float('inf')] * (n + 1)
            dist[start] = 0
            
            while pq:
                current_dist, current_node = heapq.heappop(pq)
                
                # If we found a shorter path to this node, skip it
                if current_dist > dist[current_node]:
                    continue
                
                # Explore neighbors
                for neighbor, weight in graph[current_node]:
                    new_dist = current_dist + weight
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor))
            
            return dist
        
        # Calculate the minimum cost for each starting city
        answer = []
        for start in range(1, n + 1):
            # Get the shortest distance from the start city to all other cities
            dist = dijkstra(start)
            # Calculate the minimum cost to buy an apple and return
            min_cost = float('inf')
            for city in range(1, n + 1):
                # Cost to buy an apple in city + cost to go to city + cost to return from city
                total_cost = appleCost[city - 1] + dist[city] * (1 + k)
                min_cost = min(min_cost, total_cost)
            answer.append(min_cost)
        
        return answer

def minCost(n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
    return Solution().minCost(n, roads, appleCost, k)