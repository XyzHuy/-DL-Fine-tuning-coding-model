import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        # Build the graph
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        # Initialize the DP table and the path table
        length = len(targetPath)
        dp = [[float('inf')] * n for _ in range(length)]
        path = [[-1] * n for _ in range(length)]
        
        # Base case: Initialize the first row of the DP table
        for city in range(n):
            dp[0][city] = int(names[city] != targetPath[0])
        
        # Fill the DP table
        for i in range(1, length):
            for city in range(n):
                for neighbor in graph[city]:
                    cost = dp[i - 1][neighbor] + int(names[city] != targetPath[i])
                    if cost < dp[i][city]:
                        dp[i][city] = cost
                        path[i][city] = neighbor
        
        # Find the minimum edit distance
        min_distance = float('inf')
        last_city = -1
        for city in range(n):
            if dp[-1][city] < min_distance:
                min_distance = dp[-1][city]
                last_city = city
        
        # Reconstruct the path
        result = []
        for i in range(length - 1, -1, -1):
            result.append(last_city)
            last_city = path[i][last_city]
        
        return result[::-1]

def mostSimilar(n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
    return Solution().mostSimilar(n, roads, names, targetPath)