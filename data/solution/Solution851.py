import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # Create a graph from the richer relationships
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)
        
        n = len(quiet)
        answer = [-1] * n
        
        def dfs(person):
            if answer[person] == -1:
                answer[person] = person
                for neighbor in graph[person]:
                    candidate = dfs(neighbor)
                    if quiet[candidate] < quiet[answer[person]]:
                        answer[person] = candidate
            return answer[person]
        
        # Process each person to find the quietest person with more or equal money
        for i in range(n):
            dfs(i)
        
        return answer

def loudAndRich(richer: List[List[int]], quiet: List[int]) -> List[int]:
    return Solution().loudAndRich(richer, quiet)