import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_count = defaultdict(int)
        
        for row in wall:
            total = 0
            # We don't consider the last brick in the row to avoid the outer edge
            for brick in row[:-1]:
                total += brick
                edge_count[total] += 1
        
        # Find the maximum number of edges at any position
        max_edges = max(edge_count.values()) if edge_count else 0
        
        # The minimum number of crossed bricks is the total number of rows minus the max edges
        return len(wall) - max_edges

# Example usage:
# sol = Solution()
# print(sol.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))  # Output: 2
# print(sol.leastBricks([[1],[1],[1]]))  # Output: 3

def leastBricks(wall: List[List[int]]) -> int:
    return Solution().leastBricks(wall)