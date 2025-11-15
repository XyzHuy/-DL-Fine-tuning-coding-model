import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict, deque
from typing import List

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # Step 1: Build the graph and in-degree array
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for prev, next in relations:
            graph[prev - 1].append(next - 1)
            in_degree[next - 1] += 1
        
        # Step 2: Initialize the queue with courses having no prerequisites
        queue = deque()
        dp = [0] * n
        
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
                dp[i] = time[i]
        
        # Step 3: Process the queue
        while queue:
            current = queue.popleft()
            
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                dp[neighbor] = max(dp[neighbor], dp[current] + time[neighbor])
                
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: The result is the maximum value in dp array
        return max(dp)

def minimumTime(n: int, relations: List[List[int]], time: List[int]) -> int:
    return Solution().minimumTime(n, relations, time)