import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict, deque
from typing import List

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topologicalSort(conditions):
            graph = defaultdict(list)
            inDegree = [0] * (k + 1)
            
            # Build the graph and in-degree array
            for u, v in conditions:
                graph[u].append(v)
                inDegree[v] += 1
            
            # Initialize the queue with nodes having zero in-degree
            queue = deque([i for i in range(1, k + 1) if inDegree[i] == 0])
            order = []
            
            while queue:
                node = queue.popleft()
                order.append(node)
                for neighbor in graph[node]:
                    inDegree[neighbor] -= 1
                    if inDegree[neighbor] == 0:
                        queue.append(neighbor)
            
            # If the size of the order is not k, a cycle is detected
            if len(order) != k:
                return []
            return order
        
        # Get the topological order for rows and columns
        rowOrder = topologicalSort(rowConditions)
        colOrder = topologicalSort(colConditions)
        
        # If either order is invalid, return an empty matrix
        if not rowOrder or not colOrder:
            return []
        
        # Create a mapping from number to its position in the row and column order
        rowPos = {num: idx for idx, num in enumerate(rowOrder)}
        colPos = {num: idx for idx, num in enumerate(colOrder)}
        
        # Initialize the k x k matrix with zeros
        matrix = [[0] * k for _ in range(k)]
        
        # Fill the matrix based on the positions determined by row and column orders
        for num in range(1, k + 1):
            matrix[rowPos[num]][colPos[num]] = num
        
        return matrix

def buildMatrix(k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
    return Solution().buildMatrix(k, rowConditions, colConditions)