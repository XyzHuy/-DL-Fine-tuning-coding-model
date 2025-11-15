import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # Create a graph to represent the gardens and their connections
        graph = {i: [] for i in range(1, n + 1)}
        for x, y in paths:
            graph[x].append(y)
            graph[y].append(x)
        
        # Initialize the answer array with 0 (no flower planted)
        answer = [0] * n
        
        # Try to plant flowers in each garden
        for garden in range(1, n + 1):
            # Find the flowers used by the neighboring gardens
            used_flowers = {answer[neighbor - 1] for neighbor in graph[garden]}
            # Choose the first available flower type
            for flower in range(1, 5):
                if flower not in used_flowers:
                    answer[garden - 1] = flower
                    break
        
        return answer

def gardenNoAdj(n: int, paths: List[List[int]]) -> List[int]:
    return Solution().gardenNoAdj(n, paths)