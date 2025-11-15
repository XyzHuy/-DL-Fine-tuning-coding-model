import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        def is_point_in_circle(point, query):
            x1, y1 = point
            x2, y2, radius = query
            # Calculate the squared distance to avoid using sqrt for performance
            distance_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
            return distance_squared <= radius ** 2
        
        result = []
        for query in queries:
            count = sum(1 for point in points if is_point_in_circle(point, query))
            result.append(count)
        
        return result

def countPoints(points: List[List[int]], queries: List[List[int]]) -> List[int]:
    return Solution().countPoints(points, queries)