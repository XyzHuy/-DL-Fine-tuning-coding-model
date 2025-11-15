import random
import functools
import collections
import string
import math
import datetime


from collections import deque
from typing import List

class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        # Step 1: Build the graph
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: BFS to find the shortest path from server 0 to all other servers
        distances = [-1] * n
        distances[0] = 0
        queue = deque([0])
        
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)
        
        # Step 3: Calculate the time when the network becomes idle
        max_time = 0
        for i in range(1, n):
            round_trip_time = 2 * distances[i]  # round trip time for server i
            if round_trip_time <= patience[i]:
                # If the round trip time is less than or equal to patience, the server will stop resending after one round trip
                max_time = max(max_time, round_trip_time + 1)
            else:
                # Otherwise, calculate the last resend time and add the round trip time for the final message
                last_resend_time = (round_trip_time - 1) // patience[i] * patience[i]
                max_time = max(max_time, last_resend_time + round_trip_time + 1)
        
        return max_time

def networkBecomesIdle(edges: List[List[int]], patience: List[int]) -> int:
    return Solution().networkBecomesIdle(edges, patience)