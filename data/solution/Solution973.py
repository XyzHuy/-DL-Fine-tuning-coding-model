import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Calculate the Euclidean distance of each point from the origin and store it in a list
        # along with the point itself as a tuple (distance, point)
        distances = [(self.euclidean_distance(point), point) for point in points]
        
        # Use heapq to find the k smallest distances
        k_closest_points = heapq.nsmallest(k, distances, key=lambda x: x[0])
        
        # Extract the points from the k smallest distance tuples
        return [point for _, point in k_closest_points]
    
    def euclidean_distance(self, point: List[int]) -> float:
        # Calculate the Euclidean distance from the origin (0, 0)
        return (point[0] ** 2 + point[1] ** 2) ** 0.5

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    return Solution().kClosest(points, k)