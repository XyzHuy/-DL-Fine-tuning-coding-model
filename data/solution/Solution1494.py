import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        # Build the graph and in-degree count
        graph = [[] for _ in range(n)]
        in_degree = [0] * n
        
        for prev, next in relations:
            graph[prev - 1].append(next - 1)
            in_degree[next - 1] += 1
        
        # Use a bitmask to represent the state of taken courses
        # If the i-th bit is 1, it means course i has been taken
        
        @lru_cache(None)
        def dfs(state: int) -> int:
            # If all courses are taken, return 0
            if state == (1 << n) - 1:
                return 0
            
            # Find all courses that can be taken (in-degree == 0 and not taken)
            available = [i for i in range(n) if in_degree[i] == 0 and not (state & (1 << i))]
            
            # Sort available courses by the number of their dependencies (greedy approach)
            # This is a heuristic to try to take courses that unlock more courses first
            available.sort(key=lambda x: len(graph[x]), reverse=True)
            
            # Try all combinations of taking up to k courses from the available ones
            min_semesters = float('inf')
            for i in range(1, k + 1):
                for comb in combinations(available, i):
                    new_state = state
                    for course in comb:
                        new_state |= (1 << course)
                        for next_course in graph[course]:
                            in_degree[next_course] -= 1
                    
                    min_semesters = min(min_semesters, 1 + dfs(new_state))
                    
                    # Backtrack: reset in-degree for the next combination
                    for course in comb:
                        for next_course in graph[course]:
                            in_degree[next_course] += 1
            
            return min_semesters
        
        return dfs(0)

from itertools import combinations

def minNumberOfSemesters(n: int, relations: List[List[int]], k: int) -> int:
    return Solution().minNumberOfSemesters(n, relations, k)