import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def minDayskVariants(self, points: List[List[int]], k: int) -> int:
        # Determine the bounding box for the grid search
        min_x = min(point[0] for point in points)
        max_x = max(point[0] for point in points)
        min_y = min(point[1] for point in points)
        max_y = max(point[1] for point in points)
        
        # Function to calculate the Manhattan distance
        def manhattan_distance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        
        # Initialize the minimum days to a large number
        min_days = math.inf
        
        # Search over the bounding box
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                # Count the days for each virus variant to reach (x, y)
                days = [manhattan_distance(x, y, px, py) for px, py in points]
                # Sort the days to find the k-th smallest
                days.sort()
                # The maximum of the k smallest days is the answer for this point
                min_days = min(min_days, days[k-1])
        
        return min_days

# Example usage:
# sol = Solution()
# print(sol.minDayskVariants([[1,1],[6,1]], 2))  # Output: 3
# print(sol.minDayskVariants([[3,3],[1,2],[9,2]], 2))  # Output: 2
# print(sol.minDayskVariants([[3,3],[1,2],[9,2]], 3))  # Output: 4

def minDayskVariants(points: List[List[int]], k: int) -> int:
    return Solution().minDayskVariants(points, k)