import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        def distance(p1, p2):
            return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        
        def circle_center(p1, p2, r):
            # Midpoint of p1 and p2
            midpoint = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
            # Distance between p1 and p2
            d = distance(p1, p2)
            # If the distance between points is greater than 2 * radius, no circle of radius r can contain both points
            if d > 2 * r:
                return None, None
            # Half the distance between the points
            h = math.sqrt(r ** 2 - (d / 2) ** 2)
            # Direction vector from p1 to p2
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            # Normal vector to the line segment p1p2
            nx = -dy / d
            ny = dx / d
            # Calculate the center of the circle
            cx1 = midpoint[0] + h * nx
            cy1 = midpoint[1] + h * ny
            cx2 = midpoint[0] - h * nx
            cy2 = midpoint[1] - h * ny
            return (cx1, cy1), (cx2, cy2)
        
        def count_points_in_circle(center, r, points):
            count = 0
            for point in points:
                if distance(center, point) <= r:
                    count += 1
            return count
        
        n = len(darts)
        max_points = 1
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    center1, center2 = circle_center(darts[i], darts[j], r)
                    if center1:
                        max_points = max(max_points, count_points_in_circle(center1, r, darts))
                    if center2:
                        max_points = max(max_points, count_points_in_circle(center2, r, darts))
        
        # Check if all points can be covered by a circle of radius r centered at any of the points
        for point in darts:
            max_points = max(max_points, count_points_in_circle(point, r, darts))
        
        return max_points

def numPoints(darts: List[List[int]], r: int) -> int:
    return Solution().numPoints(darts, r)