import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def shortestPathWithHops(self, n: int, edges: List[List[int]], s: int, d: int, k: int) -> int:
        # Build the adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        # Priority queue for Dijkstra's algorithm
        pq = [(0, 0, s)]  # (current distance, number of hops, current node)
        
        # Distance array to store the shortest distance with a given number of hops
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[s][0] = 0
        
        while pq:
            current_dist, hops, node = heapq.heappop(pq)
            
            # If we reach the destination, return the current distance
            if node == d:
                return current_dist
            
            # Explore neighbors
            for neighbor, weight in adj[node]:
                # If we haven't used all hops, consider the case where we hop over this edge
                if hops < k and dist[neighbor][hops + 1] > current_dist:
                    dist[neighbor][hops + 1] = current_dist
                    heapq.heappush(pq, (current_dist, hops + 1, neighbor))
                
                # Consider the case where we do not hop over this edge
                new_dist = current_dist + weight
                if dist[neighbor][hops] > new_dist:
                    dist[neighbor][hops] = new_dist
                    heapq.heappush(pq, (new_dist, hops, neighbor))
        
        # The answer is the minimum distance to reach 'd' with any number of hops up to k
        return min(dist[d])

# Example usage:
# sol = Solution()
# print(sol.shortestPathWithHops(4, [[0,1,4],[0,2,2],[2,3,6]], 1, 3, 2))  # Output: 2
# print(sol.shortestPathWithHops(7, [[3,1,9],[3,2,4],[4,0,9],[0,5,6],[3,6,2],[6,0,4],[1,2,4]], 4, 1, 2))  # Output: 6
# print(sol.shortestPathWithHops(5, [[0,4,2],[0,1,3],[0,2,1],[2,1,4],[1,3,4],[3,4,7]], 2, 3, 1))  # Output: 3

def shortestPathWithHops(n: int, edges: List[List[int]], s: int, d: int, k: int) -> int:
    return Solution().shortestPathWithHops(n, edges, s, d, k)