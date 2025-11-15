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
import heapq

class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        def max_distance_excluding_one(points, exclude_index):
            max_dist = 0
            for i in range(len(points)):
                if i == exclude_index:
                    continue
                for j in range(i + 1, len(points)):
                    if j == exclude_index:
                        continue
                    max_dist = max(max_dist, manhattan_distance(points[i], points[j]))
            return max_dist
        
        # If all points are the same, the maximum distance is 0
        if len(set(map(tuple, points))) == 1:
            return 0
        
        n = len(points)
        if n == 3:
            # If there are only 3 points, removing any one will result in the distance between the other two
            return min(manhattan_distance(points[i], points[j]) for i in range(n) for j in range(i + 1, n))
        
        # Try removing each point and calculate the maximum distance
        min_max_dist = float('inf')
        for i in range(n):
            max_dist = max_distance_excluding_one(points, i)
            min_max_dist = min(min_max_dist, max_dist)
        
        return min_max_dist

# Optimized solution using the properties of Manhattan distance
class SolutionOptimized:
    def minimumDistance(self, points: List[List[int]]) -> int:
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        # Transform points to facilitate finding the maximum and minimum Manhattan distances
        x_plus_y = [(x + y, i) for i, (x, y) in enumerate(points)]
        x_minus_y = [(x - y, i) for i, (x, y) in enumerate(points)]
        
        # Find the two points with the maximum and minimum x+y and x-y values
        max_x_plus_y1, max_x_plus_y2 = heapq.nlargest(2, x_plus_y)
        min_x_plus_y1, min_x_plus_y2 = heapq.nsmallest(2, x_plus_y)
        max_x_minus_y1, max_x_minus_y2 = heapq.nlargest(2, x_minus_y)
        min_x_minus_y1, min_x_minus_y2 = heapq.nsmallest(2, x_minus_y)
        
        # Calculate the maximum Manhattan distance without any removal
        max_dist = max(manhattan_distance(points[max_x_plus_y1[1]], points[min_x_plus_y1[1]]),
                       manhattan_distance(points[max_x_plus_y2[1]], points[min_x_plus_y2[1]]),
                       manhattan_distance(points[max_x_minus_y1[1]], points[min_x_minus_y1[1]]),
                       manhattan_distance(points[max_x_minus_y2[1]], points[min_x_minus_y2[1]]))
        
        # Check the effect of removing each of the critical points
        for (val, i) in x_plus_y + x_minus_y:
            new_max_dist = max(manhattan_distance(points[p], points[q])
                               for (v1, p) in x_plus_y if p != i
                               for (v2, q) in x_minus_y if q != i)
            max_dist = min(max_dist, new_max_dist)
        
        return max_dist

def minimumDistance(points: List[List[int]]) -> int:
    return Solution().minimumDistance(points)