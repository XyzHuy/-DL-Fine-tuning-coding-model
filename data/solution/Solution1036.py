import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked:
            return True
        
        blocked_set = set(map(tuple, blocked))
        max_steps = len(blocked) * (len(blocked) - 1) // 2
        
        def bfs(start, end):
            queue = deque([tuple(start)])
            visited = set(queue)
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            while queue:
                x, y = queue.popleft()
                
                if (x, y) == tuple(end):
                    return True
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 10**6 and 0 <= ny < 10**6 and (nx, ny) not in visited and (nx, ny) not in blocked_set:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                
                if len(visited) > max_steps:
                    return True
            
            return False
        
        return bfs(source, target) and bfs(target, source)

def isEscapePossible(blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
    return Solution().isEscapePossible(blocked, source, target)