import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
        def in_circle(x: int, y: int, cx: int, cy: int, r: int) -> bool:
            return (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2

        # Check if any circle intersects with the left top corner (0, yCorner)
        def cross_left_top(cx: int, cy: int, r: int) -> bool:
            return (cx <= r and 0 <= cy <= yCorner) or (abs(cy - yCorner) <= r and 0 <= cx <= xCorner)

        # Check if any circle intersects with the right bottom corner (xCorner, 0)
        def cross_right_bottom(cx: int, cy: int, r: int) -> bool:
            return (abs(cx - xCorner) <= r and 0 <= cy <= yCorner) or (cy <= r and 0 <= cx <= xCorner)

        # Depth-first search to check if there's a path avoiding circles
        def dfs(i: int) -> bool:
            x1, y1, r1 = circles[i]
            if cross_right_bottom(x1, y1, r1):
                return True
            vis[i] = True
            for j, (x2, y2, r2) in enumerate(circles):
                if vis[j] or not ((x1 - x2) ** 2 + (y1 - y2) ** 2 <= (r1 + r2) ** 2):
                    continue
                if dfs(j):
                    return True
            return False

        vis = [False] * len(circles)
        
        # Check if any circle covers the start or end point
        for x, y, r in circles:
            if in_circle(0, 0, x, y, r) or in_circle(xCorner, yCorner, x, y, r):
                return False
        
        # Check if there's a path from left top to right bottom avoiding circles
        for i, (x, y, r) in enumerate(circles):
            if cross_left_top(x, y, r) and dfs(i):
                return False
        
        return True

def canReachCorner(xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
    return Solution().canReachCorner(xCorner, yCorner, circles)