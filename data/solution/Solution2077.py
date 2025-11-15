import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict
from typing import List

class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        # Create an adjacency list
        adj_list = defaultdict(set)
        for u, v in corridors:
            adj_list[u].add(v)
            adj_list[v].add(u)
        
        # Count the number of cycles of length 3
        cycle_count = 0
        for u in range(1, n + 1):
            for v in adj_list[u]:
                if v > u:  # To avoid counting the same cycle multiple times
                    for w in adj_list[v]:
                        if w > v and w in adj_list[u]:
                            cycle_count += 1
        
        return cycle_count

# Example usage:
# sol = Solution()
# print(sol.numberOfPaths(5, [[1,2],[5,2],[4,1],[2,4],[3,1],[3,4]]))  # Output: 2
# print(sol.numberOfPaths(4, [[1,2],[3,4]]))  # Output: 0

def numberOfPaths(n: int, corridors: List[List[int]]) -> int:
    return Solution().numberOfPaths(n, corridors)