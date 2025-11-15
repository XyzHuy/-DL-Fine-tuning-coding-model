import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        # Create an adjacency matrix to represent the graph
        adj_matrix = [[0] * (n + 1) for _ in range(n + 1)]
        degree = [0] * (n + 1)
        
        # Fill the adjacency matrix and calculate the degree of each node
        for u, v in edges:
            adj_matrix[u][v] = 1
            adj_matrix[v][u] = 1
            degree[u] += 1
            degree[v] += 1
        
        min_degree = float('inf')
        found_trio = False
        
        # Check all possible trios
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                for k in range(j + 1, n + 1):
                    if adj_matrix[i][j] and adj_matrix[j][k] and adj_matrix[k][i]:
                        # Calculate the degree of the trio
                        trio_degree = degree[i] + degree[j] + degree[k] - 6
                        min_degree = min(min_degree, trio_degree)
                        found_trio = True
        
        return min_degree if found_trio else -1

def minTrioDegree(n: int, edges: List[List[int]]) -> int:
    return Solution().minTrioDegree(n, edges)