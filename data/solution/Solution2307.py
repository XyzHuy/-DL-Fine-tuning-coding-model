import random
import functools
import collections
import string
import math
import datetime


from typing import List, Dict

class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        # Create a graph to represent the equations
        graph: Dict[str, Dict[str, float]] = {}
        
        for (numerator, denominator), value in zip(equations, values):
            if numerator not in graph:
                graph[numerator] = {}
            if denominator not in graph:
                graph[denominator] = {}
            
            graph[numerator][denominator] = value
            graph[denominator][numerator] = 1.0 / value
        
        # Function to perform DFS and find the value of target from start
        def dfs(start: str, target: str, visited: set) -> float:
            if start == target:
                return 1.0
            visited.add(start)
            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited)
                    if result != -1.0:
                        return result * weight
            return -1.0
        
        # Check for contradictions
        for (numerator, denominator), value in zip(equations, values):
            visited = set()
            result = dfs(numerator, denominator, visited)
            if result != -1.0 and abs(result - value) >= 1e-5:
                return True
        
        return False

def checkContradictions(equations: List[List[str]], values: List[float]) -> bool:
    return Solution().checkContradictions(equations, values)